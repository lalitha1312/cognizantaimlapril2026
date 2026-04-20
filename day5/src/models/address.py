#create address class using pydantic

from pydantic import BaseModel, Field
from src.models.customer import Customer
class Address(BaseModel):

    #we are association the address to customer
    
    customer: Customer = Field(...,pattern=".*", description="The customer associated with the address")
    street: str = Field(...,pattern=".*", description="The street address")
    city: str = Field(..., pattern=".*", description="The city of the address")
    state: str = Field(..., pattern=".*", description="The state of the address")
    zip_code: str = Field(..., pattern="^\d{5}(-\d{4})?$", description="The zip code of the address")
    country: str = Field(..., description="The country of the address")