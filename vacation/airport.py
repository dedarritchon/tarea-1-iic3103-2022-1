from .city import City


class Airport():

    def __init__(
        self, name: str, lat: float = 0, long: float = 0, city: City = None, sku=None, batch=1, expiration=1, wait=1
    ):
        self.name = name
        self.lat = lat
        self.long = long
        self.city = city
        self.id = str(self) if sku is None else sku
        self.name = str(self) if name is None else name
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
    
    @property
    def reachable_airports(self):
        reachable_countries = self.city.country.reachable_countries
        reachable_airports = []
        for country in reachable_countries:
            for city in country.cities:
                for airport in city.airports:
                    reachable_airports.append(airport)
        return reachable_airports

    def __str__(self):
        return f'Airport {self.name}'

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city.serialize(),
            'lat': self.lat,
            'long': self.long
        }
