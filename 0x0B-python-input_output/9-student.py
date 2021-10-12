#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """
    defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
    """

    def __init__(self, first_name, last_name, age):
        first_name = self.first_name
        last_name = self.last_name
        age = self.age

    def to_json(self):
        return self.__dict__
