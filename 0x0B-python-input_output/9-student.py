#!/usr/bin/python3
"""Class Student"""


class Student:
    """that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """JSON"""
        return self.__dict__
