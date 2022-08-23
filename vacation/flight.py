from datetime import datetime, timedelta
from .airport import Airport
from geopy.distance import geodesic
from .airline import Airline
from .plane import Plane
import random
import pyproj

geod_WGS84 = pyproj.Geod(ellps='WGS84')


def get_flight_path(startlong, startlat, endlong, endlat):

    (_, _, dist) = geod_WGS84.inv(startlong, startlat, endlong, endlat)

    lonlats = geod_WGS84.npts(
        startlong,
        startlat,
        endlong,
        endlat,
        1 + int(dist / 10000),
        initial_idx=0,
        terminus_idx=0
    )

    return lonlats


class Flight():

    SPEED = 860
    ARRIVE_DISTANCE = 1
    ARRIVE_HOURS = 0.000000001

    def __init__(
        self, airline: Airline, departure: Airport, departure_date: datetime, destination: Airport, sku=None, batch=1, name=None, expiration=1, wait=1
    ):
        self.captain = None
        self.airline = airline
        self.departure = departure
        self.departure_date = departure_date
        self.destination = destination
        self.id = self.get_flight_id()
        self.name = str(self) if name is None else name
        self.batch = batch
        self.expiration = expiration
        self.wait = wait
        self.lat = departure.lat
        self.long = departure.long
        self.heading_lat = destination.lat
        self.heading_long = destination.long
        self.step_lat = 0
        self.step_long = 0
        self.ETA = 0
        
        self.arrival_date = 0
        self.arrived = False
        self.takeoff = False
        self.crashed = False
        self.can_crash = False
        self.status = 'take-off'
        self.flight_route_index = 0
        self.flight_route = []
        self.total_distance = self.get_travel_distance()
        self.flight_route = self.get_flight_route()

    def get_flight_route(self):
        lonlats = self.get_flight_path()
        return [[lonlat[1], lonlat[0]] for lonlat in lonlats]

    def get_flight_path(self):

        dist = self.get_travel_distance()

        lonlats = geod_WGS84.npts(
            self.long,
            self.lat,
            self.heading_long,
            self.heading_lat,
            1 + int(dist / 10000),
            initial_idx=0,
            terminus_idx=0
        )

        return lonlats

    def get_flight_id(self):
        return f'{self.departure.id}{self.airline.id}{self.destination.id}'

    def get_travel_hours(self):
        distance = self.get_travel_distance()
        return distance/self.SPEED

    def get_travel_distance(self):
        (_, _, dist) = geod_WGS84.inv(self.long, self.lat, self.heading_long, self.heading_lat)
        return dist

    def get_arrival_date(self):
        return self.departure_date + timedelta(hours=self.get_travel_hours())

    def get_info(self):

        distance = self.get_travel_distance()

        if not self.can_crash and distance/self.total_distance <= 0.5:
            self.can_crash = True

        ETA = distance/self.SPEED

        if distance <= self.ARRIVE_DISTANCE or ETA <= self.ARRIVE_HOURS:
            self.arrived = True

        arrival = self.departure_date + timedelta(hours=ETA)
        return {
            'ETA': ETA,
            'distance': distance,
            'arrival': str(arrival),
            'status': self.status
        }

    @property
    def coords(self):
        return (self.lat, self.long)

    def fly(self):
        if self.flight_route_index <= len(self.flight_route) - 1:
            self.lat = self.flight_route[self.flight_route_index][0]
            self.long = self.flight_route[self.flight_route_index][1]
            self.flight_route_index += 1

    @property
    def price(self):
        return 0

    @property
    def size(self):
        return 0

    def __str__(self):
        return f'Flight {self.id}'
    
    def change_direction(self, lat, long):
        self.heading_lat = lat
        self.heading_long = long
        self.set_steps()

    def serialize(self):
        return {
            'id': self.id,
            'airline': self.airline.serialize(),
            'departure': self.departure.serialize(),
            'destination': self.destination.serialize(),
            'departure_date': str(self.departure_date),
            'info': self.get_info(),
            'captain': self.captain if self.captain is not None else None,
            'position': {
                'lat': self.lat,
                'long': self.long,
            },
            'heading': {
                'lat': self.heading_lat,
                'long': self.heading_long
            }
        }

    def details(self):
        return {
            'id': self.id,
            'departure': self.departure.serialize(),
            'destination': self.destination.serialize(),
            'departure_date': str(self.departure_date),
        }

    def position(self):
        return {
            'flight_id': self.id,
            "position": {
                "lat": self.lat,
                "long": self.long
            },
            "heading": {
                "lat": self.heading_lat,
                "long": self.heading_long
            },
            'captain': self.captain if self.captain is not None else None,
            'airline': self.airline.serialize(),
            **self.get_info()
        }