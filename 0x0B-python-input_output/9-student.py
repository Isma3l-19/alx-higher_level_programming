#!/usr/bin/python3

"""class representing a student"""


class Student:
    """a class student"""

    def __init__(self, first_name, last_name, age):
        """initialization of the attributes

        Args:
            first_name (str): first name of student
            last_name (str): last name of student
            age (int): age of student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age= age

    def to_json(self):
        """gets the dictonary representation ofstudent"""
        return self.__dict__
