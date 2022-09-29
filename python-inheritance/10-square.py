#!/usr/bin/python3
"""Write a class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a Class"""
    def __init__(self, size):
        """Instantiation with size"""
        self.__size = self
        super().integer_validator("size", size)
        super().__init__(size, size)
