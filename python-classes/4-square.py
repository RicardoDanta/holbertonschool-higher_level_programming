#!/usr/bin/python3
"""Write a class Square that defines a square"""


class Square():
    """Define a Class"""
    def __init__(self, size=0):
        """Instantiation with optional"""
        self.size = size

    @property
    def size(self):
        """Property"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be > = 0")
        self.__size = value

    def area(self):
        """Define the Area"""
        return self.__size * self.__size
