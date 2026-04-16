# Define Doctor model

class Doctor:
    def __init__(self, name: str, department: str, phone: str):
        self.name = name
        self.department = department
        self.phone = phone

    def __str__(self):
        return f"Doctor(name={self.name}, department={self.department}, phone={self.phone})"
