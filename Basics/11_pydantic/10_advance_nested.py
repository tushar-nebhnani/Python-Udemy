"""
    Advancd Nested Model: 

    1. Optional Nested Model
    2. Mixed Datatypes
    3. Deeply Nested Structure
"""
from pydantic import BaseModel
from typing import Optional, List, Union

# Optional Nested Model
class Address(BaseModel):
    street: str
    city: str
    postal_code: str 

class Company(BaseModel):
    name: str
    address: Optional[Address] = None 

class Employee:
    name: str
    company: Optional[Company] = None

# Mixed Datatypes
class TextContent(BaseModel):
    type: str = "text" # another way of writing things
    content: str 

class ImageContent(BaseModel):
    type: str = "Image"
    url: str

class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]

# Deeply Nested Structure
class Country(BaseModel):
    name: str
    code: str

class State(BaseModel):
    name: str
    country: Country

class City(BaseModel):
    name: str
    state: State

class Address(BaseModel):
    street: str
    city: City
    postal_code: str

class Organisation:
    name: str 
    head_quarter: Address
    branches: List[Address] = []