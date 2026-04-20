#create class individual using pydantic
from datetime import datetime
from pydantic import Feild
from pydantic import FeildValidator
from pydantic import BaseModel, Field       
from src.models.customer import Customer
from src.models.gender import Gender

class Individual(BaseModel):
    
    gender: Gender
    dob: datetime.date = Field(..., description="The date of birth of the individual")


    @FeildValidator('dob')
    def validate_dob(cls, value):
        if value > datetime.date.today():
            raise ValueError("Date of birth cannot be in the future")
        return value

        age= (datetime.date.today() - value).days // 365
        if age < 18:
            raise ValueError("Individual must be at least 18 years old")
        return value