
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from .city import City
    from .airline import Airline

class Country():

    def __init__(
        self, name: str, sku=None, batch=1, expiration=1, wait=1
    ):
        self.name = name
        self.cities: List[City] = []
        self.id = str(self) if sku is None else sku
        self.batch = batch
        self.expiration = expiration
        self.wait = wait
        self.airlines: List[Airline] = []
        self.reachable_countries: List[Country] = set()
    
    def add_city(self, city):
        self.cities.append(city)
        city.country = self
    
    def add_airline(self, airline):
        self.airlines.append(airline)
        airline.country = self
    
    def add_neighbor(self, country):
        self.reachable_countries.add(country)
        country.reachable_countries.add(self)

    @property
    def price(self):
        return 0

    @property
    def size(self):
        return 0

    def __str__(self):
        return f'{self.name}'

    def __repr__(self):
        return f'{self.name}'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name
        }
