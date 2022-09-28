#!/usr/bin/python3
"""Write a class Rectangle that inherits from BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define a Class"""
    def __init__(self, width, height):
        """Instantiation"""
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
