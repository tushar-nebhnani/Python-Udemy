from pydantic import BaseModel
from typing import List, Dict, Optional

# We can create a datatype by borrowing datatypes from both typing and pydantic

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]

class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None # blog can have image or it cannot have that's why we user Optional which is a type of str and has a default value of None

cart_data = {
    "user_id": 1, 
    "items": ["Brush", "Food", "Toiletries"], 
    "quantities": {
        "Brush": 1, 
        "Food": 3, 
        "Toiletries": 10
    }
}

cart = Cart(**cart_data) # unpacking of the dictionary

