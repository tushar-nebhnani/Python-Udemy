from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    user_name: str 

    # customize validation
    @field_validator('user_name')
    # cls -> class parameter, v -> actual value which user passes
    def username_length(cls, v):
        if len(v) < 4:
            raise ValueError("Username must be at least 4 characters.")
        return v # always ensure to return the values
    
class SignUpData(BaseModel):
    password: str
    confirm_password: str 

    # Model validation
    # mode=after => run after all the field validation
    @model_validator(mode='after')
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Password do not match.")
        return values