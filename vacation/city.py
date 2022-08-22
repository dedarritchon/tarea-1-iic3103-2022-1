from typing import List, TYPE_CHECKING
from .country import Country


if TYPE_CHECKING:    
    from .airport import Airport
    from .turism import Turism
    from .hotel import Hotel


class City():

    def __init__(
        self, name: str, country: Country = None, sku=None, batch=1, expiration=1, wait=1
    ):
        self.name = name
        self.country = country
        self.airports: List[Airport] = []
        self.turisms: List[Turism] = []
        self.hotels: List[Hotel] = []
        self.id = str(self) if sku is None else sku
        self.batch = batch
        self.expiration = expiration
        self.wait = wait
    
    def add_airport(self, airport):
        self.airports.append(airport)
        airport.city = self
    
    def add_hotel(self, hotel):
        self.hotels.append(hotel)
        hotel.city = self
    
    def add_turism(self, turism):
        self.turisms.append(turism)
        turism.city = self

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
            'name': self.name,
            'country': self.country.serialize()
        }
