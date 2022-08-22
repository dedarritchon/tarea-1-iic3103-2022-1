
class Quantity():

    def __init__(self, ingredient, quantity):
        self.ingredient = ingredient
        self.quantity = quantity
    
    @property
    def id(self):
        return self.ingredient.id
    
    @property
    def name(self):
        return self.ingredient.name
    
    @property
    def batch(self):
        return self.ingredient.batch
    
    @property
    def wait(self):
        return self.ingredient.wait
    
    @property
    def price(self):
        return self.ingredient.price * self.quantity

    @property
    def size(self):
        return self.ingredient.size * self.quantity

    @property
    def expiration(self):
        return self.ingredient.expiration
    
    def serialize(self):
        serial = self.ingredient.serialize()
        serial['quantity'] = self.quantity
        return serial