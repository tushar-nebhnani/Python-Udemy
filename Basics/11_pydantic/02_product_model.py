from pydantic import BaseModel

# ALWAYS USE TYPE ANNOTATION -> NON NEGOTIABLE
class Product(BaseModel):
    id: int
    name: str
    price: float
    # Default value passing
    in_stock: bool = True

product1 = Product(id=1, name="Laptop", price=999.99, in_stock=True)
product2 = Product(id=2, name="Mouse", price=24.33)

# PyDantic always tries to convert everything to their default datatype and it can fail too, most of the times.

# Error
# Field required [type=missing, input_value={'name': 'Keyboard', 'price': 24.33}, input_type=dict]
product3 = Product(name="Keyboard", price=24.33)

