from .turism import Turism
from datetime import datetime

class TurismBooking():

    def __init__(
        self, turism: Turism, date: datetime = None, name=None, sku=None, batch=1, expiration=1, wait=1
    ):
        self.turism = turism
        self.date = date
        self.id = str(self) if sku is None else sku
        self.name = str(self) if name is None else name
        self.batch = batch
        self.expiration = expiration
        self.wait = wait

    @property
    def price(self):
        return 0

    @property
    def size(self):
        return 0

    def __str__(self):
        return f'{self.turism.id}'

    def serialize(self):
        return {
            'id': self.id,
            'turism': self.turism.serialize(),
            'date': str(self.date)
        }
