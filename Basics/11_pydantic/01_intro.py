"""
    Data Validation and Parsing. Setting and Configuration Management.
    Data serilaization/deserilaization.

    Stop the data interchangeablity of the data types.
    name = "tushar"
    name = 87 
    ❌ This is not allowed in pydantic.


    BEST PRACTICES:
    1. Define Leaf Model First - Model with no dependencies
    2. Build upward - Gradually compose more complex model
    3. Use clear naming - Easier than it look
    4. Group all related models together, try to keep them in the same file
    5. Performance Consideration - use model.dump(), deep nested level can reduce performance
    6. LArge list of nested model -> consider pagination
    7. Circular references - Can create memory heap and use the memory, recurrsive references
    8. Lazy Loading - expensive nested computation

    DATA MODELING TIPS:
    1. Real-world Relantionships
    2. Use Optional appropiately
    3. Conside UNION types
    4. Validate business rules
"""
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    is_active: bool

input_data = {'id': 101, "name": "tushar", "is_active": True}
"""
    DATA VALIDATION THROUGH PYDANTIC:
    Pydantic tries to convert the datatype into the mentioned datatype if cannot then it is forced to raised the validation error.

    input_data = {'id': 101, "name": "tushar", "is_active": 4}  
    "
        pydantic_core._pydantic_core.ValidationError: 1 validation error for User
        is_active
    "
    
    ALWAYS PASS UNPACK DICTIONARY.
    user = User(input_data)
    "
        TypeError: BaseModel.__init__() takes 1 positional argument but 2 were given
    "
"""

# always use an unpack dictionary
user = User(**input_data)
print(user)