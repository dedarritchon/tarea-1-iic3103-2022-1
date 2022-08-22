from typing import List

from turism_booking import TurismBooking

from transportation_tickets import TransportationTicket
from flight_tickets import FlightTicket
from hotel_booking import HotelBooking



class Vacation():

    def __init__(
        self,
        flight_tickets: List[FlightTicket],
        transportation_tickets: List[TransportationTicket],
        hotel_bookings: List[HotelBooking],
        turism_bookings: List[TurismBooking],
        sku=None, batch=1, name=None, expiration=1, wait=1
    ):
        self.flight_tickets = flight_tickets
        self.transportation_tickets = transportation_tickets
        self.hotel_bookings = hotel_bookings
        self.turism_bookings = turism_bookings
        self.id = self.get_id()
        self.name = str(self) if name is None else name
        self.batch = batch
        self.expiration = expiration
        self.wait = wait
    
    def get_id(self):
        flight_tickets_id = ''.join(str(f.id) for f in self.flight_tickets)
        transportation_tickets_id = ''.join(str(t.id) for t in self.transportation_tickets)
        hotel_bookings_id = ''.join(str(h.id) for h in self.hotel_bookings)
        turism_bookings_id = ''.join(str(t.id) for t in self.turism_bookings)

        return f'{flight_tickets_id}-{transportation_tickets_id}-{hotel_bookings_id}-{turism_bookings_id}'

    @property
    def price(self):
        return 0

    @property
    def size(self):
        return 0

    def __str__(self):
        return f'{self.id}'

    def serialize(self):
        return {
            'id': self.id,
            'flight_bookings': [
                f.serialize() for f in self.flight_tickets
            ],
            'transfer_bookings': [
                t.serialize() for t in self.transportation_tickets
            ],
            'hotel_bookings': [
                h.serialize() for h in self.hotel_bookings
            ],
            'turism_bookings': [
                t.serialize() for t in self.turism_bookings
            ]
        }
