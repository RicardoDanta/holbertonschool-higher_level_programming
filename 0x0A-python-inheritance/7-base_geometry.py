#!/usr/bin/python3
"""Write a class"""


class BaseGeometry:
    """Based on the last exercise"""
    def area(self):
        raise Exception("area() is not implemented")
    """Base Geometry"""
    def integer_validator(self, name, value):

        if name == str:
            if value != int:
                raise TypeError("<name> must be an integer")
                if value <= 0:
                    raise ValueError("<name> must be greater than 0")
