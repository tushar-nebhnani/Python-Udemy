from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str 

class User(BaseModel):
    id: int
    name: str
    mail: str
    is_active: bool = True
    # datetime is not that compatible with pydantic
    created_at: datetime
    address: Address
    tags: List[str] = []

    # ConfigDict allowes us to create an output to our liking
    # (Comment it out how the datetime changes with time)
    model_config = ConfigDict(
        json_encoders={datetime: lambda v: v.strftime('%d-%m-%Y %H:%M:%S') }
    )

user = User(
    id=1,
    name="Tushar",
    mail="t@google.com",
    created_at=datetime(2024, 3, 15, 14, 30),
    address = Address(
        street = "123",
        city = "Udiapur",
        zip_code="123"
    ),
    is_active=False,
    tags=["Premium user", "Subscriber"]
)
print("=" * 30)
print(user)
print("=" * 30)
python_dict = user.model_dump() # convert sub models also into a dictionary
print(python_dict)
print("=" * 30)
json_str = user.model_dump_json() # convert model & sub model into a json encoded string
print(json_str)
print("=" * 30)