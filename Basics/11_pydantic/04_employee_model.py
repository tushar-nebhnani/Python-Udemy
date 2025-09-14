"""
    FIELD VALIDATION

    Field are used to provide for validation to the data, and for field we need to read the documentation as there are many field.
"""
from typing import Optional
from pydantic import BaseModel, Field
import re

class Employee(BaseModel):
    id: int
    # To add more validation
    name: str = Field(
        ..., # Required field
        # length of the name
        min_length=3,
        max_length=25,
        # documentation of the field
        description="Employee Name",
        examples="Tushar Nebhnani"
    ) 
    department: Optional[str] = 'General'
    salary: float = Field(
        ...,
        ge=10000, # greater than or equal to
        le=50000, # less than or equal to
        description="Annual Salary is USD."
    )

class User(BaseModel):
    email: str = Field(
        ...,
        regex=r''
    )
    phone: str = Field(..., regex=r'')
    age: int = Field(
        ...,
        ge=0,
        le=100,
        description="Age in years."
    )
    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage"
    )