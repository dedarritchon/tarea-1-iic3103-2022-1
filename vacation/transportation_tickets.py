from datetime import datetime, timedelta
from .airport import Airport
from .hotel import Hotel
from geopy.distance import geodesic
from .transportation import Transportation

class TransportationTicket():

    def __init__(
        self, transportation: Transportation, departure: Airport, departure_date: datetime, destination: Hotel, sku=None, batch=1, name=None, expiration=1, wait=1
    ):
        self.transportation = transportation
        self.departure = departure
        self.departure_date = departure_date
        self.destination = destination
        self.arrival_date = self.get_arrival_date()
        self.id = self.get_transportation_id()
        self.name = str(self) if name is None else name
        self.batch = batch
        self.expiration = expiration
        self.wait = wait
        self.lat = departure.lat
        self.long = departure.long
    
    def get_transportation_id(self):
        return f'{self.transportation.id}'

    def get_travel_hours(self):
        distance = self.get_travel_distance()
        return distance/self.transportation.SPEED
    
    def get_travel_distance(self):
        return geodesic(self.departure.coords, self.destination.coords).km

    def get_arrival_date(self):
        return self.departure_date + timedelta(hours=self.get_travel_hours())
    
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
        return f'Flight {self.id}'

    def serialize(self):
        return {
            'id': self.id,
            'company': self.transportation.serialize(),
            'departure': self.departure.serialize(),
            'destination': self.destination.serialize(),
            'departure_date': str(self.departure_date),
            'ETA': self.get_travel_hours(),
            'travel_distance': self.get_travel_distance(),
            'arrival_date': str(self.get_arrival_date()),
            'position': {
                'lat': self.lat,
                'long': self.long
            }
        }
