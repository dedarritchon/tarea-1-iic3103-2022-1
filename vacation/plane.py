
class Plane():

    SPEED = 860

    def __init__(
        self, name: str, id=None, batch=1, expiration=1, wait=1
    ):
        self.name = name
        self.id = id if id is not None else name
        self.batch = batch
        self.expiration = expiration
        self.wait = wait
        self.lat = None
        self.long = None

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
        return f'Plane {self.id}'

    def serialize(self):
        return {
            #'price': self.price,
            #'size': self.size,
            #'expiration': self.expiration,
            'id': self.id,
            'name': self.name,
            'lat': self.lat,
            'long': self.long
        }
