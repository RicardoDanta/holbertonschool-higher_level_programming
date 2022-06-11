#!/usr/bin/python3
"""Import"""

from models.base import Base
"""Inherits"""


class Rectangle(Base):
    """Constructor"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """init"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        "Width P"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height P"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X P"""
        return self.__x

    @x.setter
    def x(self, value):
        """X"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y P"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Area"""
        return self.width * self.height
