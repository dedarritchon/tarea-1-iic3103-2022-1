import random
from enum import Enum

class Range(Enum):
    low = 'l'
    avg = 'a'
    high = 'h'

class Property():

    def __init__(self, range: Range):
        self.id = f'{range.value}{self.property_id}'
        self.range = range

    @property
    def value(self):
        values = {
            Range.high: random.randint(self.high, self.max),
            Range.avg: random.randint(self.low, self.high),
            Range.low: random.randint(self.min, self.low)
        }
        return values[self.range]

class Price(Property):

    property_id = 'p'
    max = 5000
    high = 3000
    avg = 2000
    low = 1000
    min = 500


class Size(Property):

    property_id = 's'
    max = 500
    high = 400
    avg = 300
    low = 200
    min = 100


class Expiration(Property):

    property_id = 'e'
    max = 10
    high = 8
    avg = 6
    low = 5
    min = 3
