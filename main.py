from importlib.machinery import SourcelessFileLoader
from google.cloud import bigquery
from datetime import datetime, timedelta
from typing import Dict, List, Optional
from http import HTTPStatus
import websockets
import traceback
import asyncio
import secrets
import random
import names
import json
import os

from itertools import filterfalse

from vacation.mixin import airlines, airports
from vacation.flight import Flight


from utils import USERS
from questions import SAMPLE_QUESTIONS


PORT = int(os.getenv('PORT', 8000))
HOST = 'trivia.tallerdeintegracion.cl'


class Question():

    def __init__(
        self, question_id: int,
        type: str = 'text', title: str = None,
        options: Dict[int, str] = {},
        answer: str = None,
        wait: int = 10, points: int = 1
    ):
        self.id = question_id
        self.type = type
        self.title = title
        self.options = options
        self.answer = answer
        self.wait = wait
        self.points = points
        self.active = False
        self.correct = 0
        self.randomize()

    def __str__(self):
        return f'Q{self.id}: {self.title}'

    def serial(self, internal=False):
        serial = {
            'type': 'question',
            'question_id': self.id,
            'question_type': self.type,
            'question_title': self.title,
            'question_points': self.points,
            'question_options': self.options
        }
        if internal:
            serial['active'] = self.active
            serial['wait'] = self.wait
            serial['correct'] = self.correct

        return serial

    def start(self):
        self.active = True
    
    def stop(self):
        self.active = False

    def is_active(self):
        return self.active
    
    def remaining(self, seconds_passed: int) -> Dict:
        return {
            'type': 'timer',
            'question_id': self.id,
            'seconds_remaining': self.wait - seconds_passed
        }

    def is_button(self):
        return self.type == 'button'

    def is_text(self):
        return self.type == 'text'

    def is_chat(self):
        return self.type == 'chat'
    
    def randomize(self):
        if self.is_button():
            print("shuffling button question")
            print(f"before shuffle: {self.options}, R:{self.answer}")
            new_options = {}
            old_answer = self.options[self.answer]
            old_options = list(self.options.values())

            random.shuffle(old_options)

            for i in range(len(old_options)):
                new_options[i+1] = old_options[i]
                if old_answer == old_options[i]:
                    self.answer = i+1

            self.options = new_options

            print(f"after shuffle: {self.options}, R:{self.answer}")


class QuestionFactory():

    @classmethod
    def new(cls, question_id: int):
        question_params = cls.get_random_params()
        return Question(question_id, **question_params)

    @classmethod
    def get_random_params(cls):
        return random.choice(SAMPLE_QUESTIONS)


class User():

    def __init__(self, socket=None, id=None, username=''):
        self.id = str(id) if id is not None else secrets.token_urlsafe(10)
        self.username = str(username)
        self.socket = socket
        self.score = 0
        self.streak = 0
        self.answered = False
        self.correct = False
        self.flight: Optional[Flight] = None

    def __str__(self):
        return self.username

    def reset(self):
        self.score = 0
        self.streak = 0
        self.answered = False

    def serial(self):
        return {
            'username': self.username,
            'score': self.score,
            'streak': self.streak
        }
    
    def serialize(self):
        return {
            'id': self.id,
            'name': self.username
        }

    async def send(self, message):
        await self.socket.send(json.dumps(message))
    
    ######### Client Mock (see users.py) ##########

    async def join_network(self):
        self.socket = await websockets.connect('ws://localhost:8000/connect')
        await self.send({'type': 'join', 'id': self.id, 'username': self.username})
        await self.listen()

    async def listen(self):
        async for message in self.socket:
            try:
                event = json.loads(message)
                self.log(f'Got event: {event}')
                type = event.get('type')
                if type == 'question':
                    question_id = event.get('question_id')
                    options = event.get('question_options')
                    options = [1, 2, 3, 4]
                    answer = random.choice(options)
                    await self.send({
                        'type': 'answer',
                        'question_id': question_id,
                        'value': answer
                    })

            except Exception as e:
                self.log(e)
                pass
        self.log(f'{self} disconnected from server')

    def log(self, message):
        print(f'[User {self.username}] {message}')


class Room():

    MAX_FLIGHTS = int(os.getenv('MAX_FLIGHTS', 1))
    MAX_CLIENTS = 150
    LOBBY_WAIT = 10

    def __init__(self):
        self.id = secrets.token_urlsafe(10)
        self.clients = {}
        self.flights = {}
        self.lobby_wait = self.LOBBY_WAIT
        self.created = str(datetime.utcnow())

    def general_info(self):
        return {
            'room_id': self.id,
            'message': f'Join via wss://{HOST}/connect'
        }

    def flights_event(self):
        return {
            'type': 'flights',
            'flights' : {f.id: f.details() for f in self.get_flights()}
        }
    
    def plane_event(self, flight):
        return {
            'type': 'plane',
            'plane': flight.position()
        }

    def message_event(self, content, level, username, flight_id=None):
        return {
            'type': 'message',
            'message' : {
                'flight_id': flight_id,
                'level': level,
                'content': content,
                'date': str(datetime.utcnow()),
                'name': username
            }
        }

    def get_flights(self):
        return self.flights.copy().values()

    def flights_info(self):
        return {
            f.id: f.details() for f in self.get_flights()
        }
    
    def random_takeoff_message(self, flight: Flight):
        selected = random.choice([
            'Preparing for takeoff',
            "Let's kick the tires and light the fires",
            'Cleared for Take-off',
            f'Leaving {flight.departure.name}',
            'Flight attendants, prepare for take-off please.',
            f'Our flight time will be of {flight.get_travel_hours()} hours',
            'Cabin Crew, please prepare for gate departure.',
            'Flight attendants, doors on automatic, cross-check and report. Thank you.',
            'Flight attendants, prepare for take-off please.',
            'Cabin crew, please take your seats for take-off.',
            'Now we request your full attention as the flight attendants demonstrate the safety features of this aircraft'
        ])
        return selected
    
    def random_landing_message(self, flight: Flight):
        selected = random.choice([
            'Landed safely',
            f'Landed at {datetime.utcnow()}',
            'Deploying landing gear',
            f'Ladies and gentlemen, welcome to {flight.destination.city.country.name}. Local time is {datetime.utcnow()} and the temperature is {random.randint(20,36)}°C',
            'Landing gear deployed',
            'light attendants, prepare for landing please.',
            f'Ladies and gentlemen, we have just been cleared to land at the {flight.destination.name} airport.',
            'Ladies and gentlemen, as we start our descent, please make sure your seat backs and tray tables are in their full upright position',
            'Make sure your seat belt is securely fastened and all carry-on luggage is stowed underneath the seat in front of you or in the overhead bins. Thank you.'
        ])
        return selected
    
    def random_crash_message(self, flight: Flight):
        selected = random.choice([
            'Mayday Mayday',
        ])
        return selected
    
    def random_flying_message(self, flight: Flight):
        selected = random.choice([
            'Flight conditions are OK',
            "We're flying through an air pocket",
            "Ladies and gentlemen, we're experiencing some turbulence. Please return to your seats and fasten your seatbelts",
            'We are now crossing a zone of turbulence. Please return your seats and keep your seat belts fastened. Thank you.',
            'Radio receptions are loud and clear',
            f'Approaching {flight.destination.id} Airport',
            f'We are {flight.get_travel_distance()} km from our destination',
            f'There are {random.randint(100, 200)} souls on board',
            f'Estimated time of arrival: {int(flight.get_travel_hours())} hours',
            'Ladies and gentlemen, the Captain has turned on the Fasten Seat Belt sign',
            'If you are seated next to an emergency exit, please read carefully the special instructions card located by your seat.',
            'Smoking is prohibited on the entire aircraft, including the lavatories.',
            f'We are flying at an altitude of {random.randint(8000, 10000)} meters at a ground speed of {random.randint(700, 900)} miles per kilometers per hour.'
        ])
        return selected


    async def send_plane_events(self):
        await asyncio.gather(
            *[self.broadcast(self.plane_event(f)) for f in self.get_flights()]
        )

    async def simulate(self, flight: Flight):
        
        await self.simulate_takeoff(flight)

        await self.simulate_flying(flight)
    
    async def simulate_takeoff(self, flight: Flight):
        while True:
            # preparing for takeoff
            if random.random() <= 0.5:
                if random.random() <= 0.1:
                    await self.broadcast(
                        self.message_event(
                            self.random_takeoff_message(flight),
                            'info', flight.captain, flight_id=flight.id
                        )
                    )
                await asyncio.sleep(5)
                continue
            await self.broadcast(self.takeoff_event(flight))
            
            break

    async def simulate_flying(self, flight: Flight):
        flight.status = 'flying'
        while True:

            flight.fly()

            if random.random() <= 0.002:
                await self.broadcast(
                    self.message_event(
                        self.random_flying_message(flight),
                        'info', flight.captain, flight_id=flight.id
                    )
                )

            if flight.can_crash and random.random() <= 0.0001:
                await self.simulate_crash(flight)
                break

            if flight.arrived:
                await self.simulate_landing(flight)
                break

            await asyncio.sleep(0.2)

    async def simulate_crash(self, flight: Flight):
        flight.status = 'crashed'
        await self.broadcast(self.crash_event(flight))
        await self.broadcast(
            self.message_event(
                self.random_crash_message(flight),
                'warn', flight.captain, flight_id=flight.id
            )
        )
        await asyncio.sleep(10)
        self.remove_flight(flight)

    async def simulate_landing(self, flight: Flight):
        flight.status = 'arrived'
        await self.broadcast(self.landing_event(flight))

        if random.random() <= 0.1:
            await self.broadcast(
                self.message_event(
                    self.random_landing_message(flight),
                    'info', flight.captain, flight_id=flight.id
                )
            )

        await asyncio.sleep(5)
        self.remove_flight(flight)

    def landing_event(self, flight: Flight):
        return {
            'type': 'landing',
            'flight_id': flight.id
        }
    
    def takeoff_event(self, flight: Flight):
        return {
            'type': 'take-off',
            'flight_id': flight.id
        }
    
    def crash_event(self, flight: Flight):
        return {
            'type': 'crashed',
            'flight_id': flight.id
        }

    def log(self, message: str):
        print(f'[Room {self.id}] {message}')

    def size(self):
        return len(self.clients.keys())

    def is_full(self):
        return len(self.clients.keys()) >= self.MAX_CLIENTS

    def is_empty(self):
        return len(self.clients.keys()) == 0

    def get_users(self):
        return list(self.clients.values())

    def get_questions(self):
        return list(self.questions.values())

    def scoreboard(self):
        return {
            'type': 'score',
            'scores' : {p.username: p.score for p in self.get_users()}
        }

    def denied_event(self, message: str):
        return {
            'type': 'denied',
            'trivia_id': self.id,
            'reason': message
        }

    def denied_invalid_payload(self):
        return self.denied_event('you sent an unexpected or invalid payload')

    def denied_MAX_CLIENTS_reached(self):
        return self.denied_event('Room is full. Please try again later')

    def denied_invalid_id(self):
        return self.denied_event('Please use a valid join id')

    def denied_already_connected(self, user):
        return self.denied_event(f'User with id {user.id} already connected')

    def denied_username_taken(self, user):
        return self.denied_event(f'Username {user.username} is already taken')

    def reset_event(self):
        return {
            'type': 'reset',
            'trivia_id': self.id
        }

    async def reset(self):

        self.lobby_wait = self.LOBBY_WAIT

        for user in self.get_users():
            user.reset()


    async def broadcast(self, message: str):
        # self.log(f'Brodcasting: {message}')
        await asyncio.gather(
            *[p.send(message) for p in self.get_users()]
        )

    async def start(self):
        async with websockets.serve(
            self.join_handler, '0.0.0.0', PORT, process_request=self._http_handler
        ):
            self.log(f'Running Websocket Server on port {PORT}')
            await asyncio.gather(
                self.plane_events_loop(),
                self.create_flights_loop(),
                asyncio.Future() # run forever
            )

    async def listen(self, user: User):
        async for message in user.socket:
            self.log(f'{user.username} sent {message}')
            try:
                event = json.loads(message)
                self.log(f'Got user event: {event}')
                type = event.get('type')

                content = event.get('content')

                if type == 'chat' and content:
                    await self.handle_chat_event(user, event)

            except Exception as e:
                self.log(f'Exception on user {user.id} listen: {e}')
                raise e
    
    async def handle_chat_event(self, user: User, event):
        content = event.get('content')
        if (isinstance(content, str)) and len(content) < 100:
            await self.broadcast(self.message_event(
                    content,
                    'info',
                    user.username
                ))

    def get_question_points(self, question: Question) -> int:
        if question.is_chat() and self.size() != 0:
            return question.points * ( 1 - question.correct/self.size()) 
        return question.points

    def answer_is_correct(self, question: Question, value) -> bool:
        answer = str(value).lower().replace(' ', '')
        expected = str(question.answer).lower().replace(' ', '')
        print(f"expected: {expected}, received: {answer}")
        return answer == expected

    def correct_answer_event(self, question: Question):
        return self.answer_event(question, True)

    def incorrect_answer_event(self, question: Question):
        return self.answer_event(question, False)

    def answer_event(self, question: Question, result: bool):
        return {
            'type': 'result',
            'question_id': question.id,
            'correct': result
        }

    def chat_question_answer_event(self, question: Question, user: User, value: str):
        return {
            'type': 'chat',
            'question_id': question.id,
            'message': value,
            'username': user.username,
            'timestamp': str(datetime.utcnow())
        }

    def streak_event(self, user: User):
        return {
            'type': 'streak',
            'username': user.username,
            'streak': user.streak 
        }
    
    def add_flight(self, flight):
        self.flights[flight.id] = flight

    def remove_flight(self, flight):
        self.flights.pop(flight.id, None)

    def generate_random_flight(self):

        departure_airport, destination_airport = random.sample(airports, 2)

        departure_date = datetime.utcnow() + timedelta(days=random.randint(30, 90))

        airline = random.choice(airlines)

        flight =  Flight(airline, departure_airport, departure_date, destination_airport)

        flight.captain = names.get_full_name()

        flight.id = f'{flight.id}{random.randint(100,200)}'

        return flight

    def log_results_to_bigquery(self):

        rows = [
            self.results_to_row(p)
            for p in self.get_users()
        ]

        try:
            self.insert_to_big_query(rows)
        except Exception as e:
            self.log(f"Error while inserting to BQ: {e}")

    
    def insert_to_big_query(self, rows):
        table_id = "growth-charts-dev.taller_integracion_2022_1.tarea_2_2022_1_results"
        client = bigquery.Client()
        print(f'Inserting to BQ: {table_id}')
        errors = client.insert_rows_json(table_id, rows)
        if len(errors) == 0:
            print("New rows have been added.")
        else:
            print(f"Encountered errors while inserting rows: {errors}")

    def results_to_row(self, user: User):
        return {
            "created": self.created,
            "trivia_id": self.id,
            "user_id": user.id,
            "user_username": user.username,
            "user_score": user.score,
            "user_streak": user.streak
        }

    def winners(self):
        self.lobby_wait = 1 # patch to stop sending scores event
        return {
            'type': 'highscore',
            'winners': self.get_top_3()
        }

    def get_top_3(self):
        sort = list(sorted(self.get_users(), key=lambda p: p.score, reverse=True))[:3]
        return [p.serial() for p in sort]
    
    async def plane_events_loop(self):
        while True:
            await self.send_plane_events()
            await asyncio.sleep(0.5)
    
    async def create_flights_loop(self):
        while True:
            if len(self.get_flights()) >= self.MAX_FLIGHTS:
                pass
            else:
                try:
                    flight = self.generate_random_flight()
                    self.add_flight(flight)
                    asyncio.create_task(self.simulate(flight))
                except:
                    self.remove_flight(flight)

            await self.broadcast(self.flights_event())
            await asyncio.sleep(1)


    async def lobby_sleep(self, seconds: int):
        self.lobby_wait -= seconds
        await asyncio.sleep(seconds)

    def lobby_wait_event(self):
        message = f'Waiting {self.lobby_wait} seconds for other users to join'
        self.log(message)
        return {
            'type': 'lobby',
            'message': message,
            'seconds_remaining': self.lobby_wait,
            'users': [p.username for p in self.get_users()]
        }

    async def questions_loop(self):
        self.generate_questions()
        await self.ask_questions()

    def generate_questions(self):
        for id in range(self.QUESTIONS):
            question = QuestionFactory.new(id)
            self.questions[question.id] = question

    async def ask_questions(self):
        for question in self.questions.values():
            self.log(f'Asking question {question.id}: {question.serial()}')
            self.reset_users_status()
            await self.ask_question(question)

    async def ask_question(self, question: Question):
        self.current_question = question
        question.start()
        await self.broadcast(question.serial())
        for i in range(question.wait):
            if not question.is_chat() and self.all_users_answered():
                break
            if self.size() and question.is_chat() and question.correct/self.size() > 0.1:
                break
            self.log(f"Waiting time for question {question.id}: {question.wait - i}")
            await self.broadcast(question.remaining(i))
            await asyncio.sleep(1)
        question.stop()
        self.current_question = None

    def all_users_answered(self):
        return all([p.answered for p in self.get_users()])

    def reset_users_status(self):
        for user in self.get_users():
            user.answered = False
            user.correct = False

    async def handle_disconnect(self, user):
        try:
            self.clients.pop(user.id, None)
            # socket may be disconnected already
            await user.send(self.disconnect_event())
            await user.socket.close()
        except:
            pass

        self.log(f'{user.id} disconnected from server')

    def disconnect_event(self):
        return {
            "type": "disconnected",
            "trivia_id": self.id,
            "message": "You have been disconnected from the Room. PLease follow the rules"
        }

    async def join_handler(self, websocket):
        try:
            node = User(websocket)
            message = await websocket.recv()
            event = json.loads(message)
            type = event.get('type')
            id = event.get('id', '')
            username = event.get('username', '')

            print(f"######## GOT EVENT: {event}")

            if username == '':
                username = USERS.get(id, '')
 
            if not isinstance(username, str):
                raise Exception("Username must be a string")
            
            if len(username) > 40:
                raise Exception("Username must be shorter than 40 chars")

            if all([type == 'join', id]):
                node.id = id
                node.username = username[:40]
                await self.add_user(node)
                await self.listen(node)
            else:
                await node.send(self.denied_invalid_payload())

        except Exception as e:
            self.log(f'Error handling {node.id}: {e}, terminating')
        finally:
            await self.handle_disconnect(node)

    async def add_user(self, user: User):

        await self.check_valid_join(user)

        self.clients[user.id] = user
        user.network = self

        await user.send(self.accepted_event())
        self.log(f'{user.id} connected to server')
    
    def accepted_event(self):
        return {
            'type': 'accepted',
            'room_id': self.id,
            'joined': self.size()
        }
    
    async def check_valid_join(self, user: User):

        if self.is_full():
            await user.send(self.denied_MAX_CLIENTS_reached())
            raise Exception('Network is full')

        if user.id in self.clients.keys():
            await user.send(self.denied_already_connected(user))
            raise Exception(f'User with id {user.id} already connected')

        if user.username in [p.username for p in self.get_users()]:
            await user.send(self.denied_username_taken(user))
            raise Exception(f'Username {user.username} is already taken')

    def health_info(self):
        return {
            'trivia_id': self.id,
            'joined': self.size(),
            'users': {p.username: p.serial() for p in self.get_users()},
            'questions': {q.id: q.serial(internal=True) for q in self.get_questions()}
        }

    async def _http_handler(self, path: str, headers: Dict):

        if 'Sec-WebSocket-Key' in headers.keys() and path == '/connect':
            return

        body = self.general_info()

        if path == '/health':
            body = self.health_info()

        if path == '/reset':
            await self.reset()
            body = self.health_info()
        
        if path == '/play':

            file_path = '/client.html'

            response_headers = [
                ('Server', 'asyncio websocket server'),
                ('Connection', 'close'),
            ]

            # Derive full system path
            full_path = '/home/dedarritchon/2022-1-tarea-2/client-js/public/index.html'

            print(full_path)

            # Guess file content type
            response_headers.append(('Content-Type', "text/html"))

            # Read the whole file into memory and send it out
            body = open(full_path, 'rb').read()
            response_headers.append(('Content-Length', str(len(body))))

            return HTTPStatus.OK, response_headers, body

        return HTTPStatus.OK, [], bytes(json.dumps(body),'UTF-8')

async def main():
    await Room().start()

if __name__ == '__main__':
    while True:
        print("Starting main execution")
        try:
            asyncio.run(main())
        except Exception as e:
            print(f"Error ocurred on main execution: {e}")
            traceback.print_exc()
