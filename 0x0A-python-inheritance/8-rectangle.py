#!/usr/bin/python3
"""Write a class"""


class BaseGeometry:
    """Based on the last exercise"""
    def area(self):
        raise Exception("area() is not implemented")
    """Base Geometry"""
    def integer_validator(self, name, value):

        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """My class Rectangle"""
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
