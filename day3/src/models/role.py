"""
role mkdel definition
"""

class Role:
    """ a classs representing a role in the hospital management system """
    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description

    #getters for role_name and role_description
    @property
    def name(self):
        return self.__name

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        self.__description = value
