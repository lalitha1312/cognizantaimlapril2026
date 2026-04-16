import typing

class Doctor:
    def __init__(self, id: int, name: str, specialty: str):
        self.id = id
        self.name = name
        self.specialty = specialty

    def __str__(self):
        return f"Doctor (id= {self.id}, name= {self.name}, specialty= {self.specialty})"