""" create class staff inherit from person and add staff specific attributes and methods """
from src.models.person import Person
from src.models.role import Role

class Staff(Person):     #inherit from person class
    """class staff"""

    def __init__(self, aadharno: int, mobileno: int,role: Role):
        super().__init__(aadharno, mobileno)
        self.__role = role    #association with role class

    @property
    def role(self):
        return self.__role
git 
    @role.setter
    def role(self, value):
        self.__role = value