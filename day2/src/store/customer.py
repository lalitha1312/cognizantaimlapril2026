# Customer model class
class Customer:
    def __init__(self, name: str, email: str, dob):
        self.name = name
        self.email = email
        self.dob = dob

    def __str__(self):
        return f"Name: {self.name}, Email: {self.email}, DOB: {self.dob}"