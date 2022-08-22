
from mixin import countries
from flight import Flight
from flight_tickets import FlightTicket
from turism_booking import TurismBooking
from hotel_booking import HotelBooking
import random

from datetime import datetime, timedelta

from rates import rates
from transportations import transportations
from transportation_tickets import TransportationTicket

from planes import some_plane

from vacation import Vacation


now = datetime.utcnow()

from datetime import timedelta
import itertools

import json


def random_date(start, end):
    """
    This function will return a random datetime between two datetime 
    objects.
    """
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = random.randrange(int_delta)
    return start + timedelta(seconds=random_second)

def to_json(payload):
    return json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)


all_vacations = {}

# all permutations
for departure_country in countries:

    for destination_country in departure_country.reachable_countries:

        cities_subsets = itertools.product(departure_country.cities, destination_country.cities)

        for cities_subset in cities_subsets:

            departure_city, destination_city = cities_subset

            airports_subsets = itertools.product(departure_city.airports, destination_city.airports)

            for airport_subset in airports_subsets:

                departure_airport, destination_airport = airport_subset

                for airline in departure_country.airlines:

                    start_date = now + timedelta(days=random.randint(30, 90))



                    flight = Flight(some_plane, airline, departure_airport, start_date, destination_airport)

                    arrival_date = flight.get_arrival_date()

                    for flight_rate in rates:

                        flight_ticket = FlightTicket(flight, flight_rate)

                        for hotel in destination_city.hotels:

                            transportation_company = random.choice(transportations)

                            transportation_ticket = TransportationTicket(transportation_company, destination_airport, arrival_date, hotel)

                            hotel_date = transportation_ticket.get_arrival_date()

                            for d in range(3, 5):

                                return_date = hotel_date + timedelta(days=d)

                                for turism in destination_city.turisms:

                                    turism_date = random_date(hotel_date, return_date - timedelta(days=1))

                                    hotel_booking = HotelBooking(hotel, hotel_date, return_date)

                                    print(f"Reserva de Hotel: {hotel_booking}")

                                    turism_booking = TurismBooking(turism, turism_date)

                                    print(f"Reserva de Turismo: {turism_booking}")

                                    #print(f"Reserva de Turismo 1: {turism_booking_1}")
                                    #print(f"Reserva de Turismo 2: {turism_booking_2}")

                                    vacation = Vacation(
                                        flight_tickets=[flight_ticket],
                                        transportation_tickets=[transportation_ticket],
                                        hotel_bookings=[hotel_booking],
                                        turism_bookings=[turism_booking],
                                    )

                                    all_vacations[vacation.id] = vacation.serialize()

                                    print(vacation.id)

print(f'Total: {len(all_vacations.keys())}')
print("#"*90)

with open(f'exports/json/vacations.json', 'w') as file:
    file.write(to_json(all_vacations))

print("file generated")