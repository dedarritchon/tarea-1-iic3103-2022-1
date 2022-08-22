from operator import lt
from .city import City


class Hotel():

    def __init__(
        self, name: str, lat: float = 0, long: float = 0, city: City = None, sku=None, batch=1, expiration=1, wait=1
    ):
        self.name = name
        self.lat = lat
        self.long = long
        self.city = city
        self.id = str(self) if sku is None else sku
        self.batch = batch
        self.expiration = expiration
        self.wait = wait

    @property
    def coords(self):
        return (self.lat, self.long)

    @property
    def price(self):
        return 0

    @property
    def size(self):
        return 0

    def __str__(self):
        return f'{self.name}'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
