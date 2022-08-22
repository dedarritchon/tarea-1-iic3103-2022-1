
class Transportation():

    SPEED = 60

    def __init__(
        self, name: str, sku=None, batch=1, expiration=1, wait=1
    ):
        self.name = name
        self.id = sku
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
        return f'Flight {self.id}'

    def serialize(self):
        return {
            #'price': self.price,
            #'size': self.size,
            #'expiration': self.expiration,
            'id': self.id,
        }
