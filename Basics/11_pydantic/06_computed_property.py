from pydantic import BaseModel, computed_field, Field

class Product(BaseModel):
    price: float
    quantity: int 

    # calculated field
    @computed_field
    @property # makes it accesible as an attribute
    def total_price(self) -> float:
        return self.price * self.quantity
    
class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_nigth: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_nigth
    
booking = Booking(
    user_id=123,
    room_id=456,
    nights=3,
    rate_per_nigth=1000.00
)

print(booking.total_amount) # this gets added into the model serialization as well
print(booking.model_dump())