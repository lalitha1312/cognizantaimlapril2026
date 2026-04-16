"""
create patient class with attributes id, name, age, and medical_history
""" 

import typing


class Patient:
    def __init__(self, id: int, name: str, age: int, ailment: list):
        self.id = id
        self.name = name
        self.age = age
        self.ailment = ailment

    def __str__(self):
        return f"Patient [id= {self.id}, name= {self.name}, age= {self.age}, ailment= {self.ailment}]"