#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle"""


class Rectangle:
    """Define a Class"""
    def __init__(self, width=0, height=0):
        """Instantiation with optional width and height"""
        self.width = width
        self.height = height

    @property
    def width(self):
        self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__size = value

    @property
    def height(self):
        self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__size = value
