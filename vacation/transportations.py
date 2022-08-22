from .transportation import Transportation

uber = Transportation('Uber', sku='T2')
cabify = Transportation('Cabify', sku='T2')
didi = Transportation('DiDi', sku='T3')
taxi = Transportation('Taxi', sku='T4')
transfer = Transportation('Transportation', sku='T5')

transportations = [
    uber, cabify, didi, taxi, transfer
]