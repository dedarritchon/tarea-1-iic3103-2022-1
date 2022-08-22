from .rate import Rate
from .flight import Flight


class FlightTicket():

    def __init__(
        self, flight: Flight, rate: Rate, sku=None, batch=1, name=None, expiration=1, wait=1
    ):
        self.flight = flight
        self.rate = rate
        self.id = self.get_id(flight, rate)
        self.name = str(self) if name is None else name
        self.batch = batch
        self.expiration = expiration
        self.wait = wait
    
    def get_id(self, flight, rate):
        return f'{flight.id}{rate.id}'

    @property
    def price(self):
        return 0

    @property
    def size(self):
        return 0

    def __str__(self):
        return f'Trip {self.id}'

    def serialize(self):
        return {
            'id': self.id,
            'flight': self.flight.serialize(),
            'rate': self.rate.serialize()
        }
