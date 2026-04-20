#create corporate class inherit from customer using pydantic

from pydantic import BaseModel, Field
from src.models.customer import Customer
from src.models.company_type import CompanyType
class Corporate(Customer):
    company_type: CompanyType
    registration_number: str = Field(..., description="The registration number of the company")