from pydantic import BaseModel
from typing import List, Optional

class Address(BaseModel):
    street: str
    city: str
    postal_code: str 

class User(BaseModel):
    id: int
    name: str 
    address: Address

address = Address(
    street="123",
    city="Udaipur",
    postal_code="1001"
)

user = User(
    id=1,
    name="tushar",
    address=address
)

user_data = {
    "id": 1,
    "name": "tushar",
    "address": {
        "street": "321",
        "city": "Jaipur",
        "postal_code": "10011"
    }
}

user = User(**user_data)
print(user)