from .hotel import Hotel
from datetime import datetime


class HotelBooking():

    def __init__(
        self, hotel: Hotel, checkin: datetime, checkout: datetime, sku=None, batch=1, name=None, expiration=1, wait=1
    ):
        self.hotel = hotel
        self.checkin = checkin
        self.checkout = checkout
        self.id = self.get_id()
        self.name = str(self) if name is None else name
        self.batch = batch
        self.expiration = expiration
        self.wait = wait

    def get_id(self):
        return f'{self.hotel.id}S{self.stay}'

    @property
    def stay(self):
        return (self.checkout - self.checkin).days

    @property
    def price(self):
        return 0

    @property
    def size(self):
        return 0

    def __str__(self):
        return f'{self.stay} x sku {self.hotel.id} {self.hotel.name}'

    def serialize(self):
        return {
            'id': self.id,
            'hotel': self.hotel.serialize(),
            'checkin': str(self.checkin),
            'checkout': str(self.checkout),
            'stay': self.stay
        }
