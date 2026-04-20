from pydantic import BaseModel, Field

class FullName(BaseModel):
    first_name: str = Field(..., pattern=r"^[a-zA-Z]+$", description="The first name of the person")
    last_name: str = Field(..., pattern=r"^[a-zA-Z]+$", description="The last name of the person")