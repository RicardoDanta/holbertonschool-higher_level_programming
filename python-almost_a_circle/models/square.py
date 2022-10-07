#!/usr/bin/python3
"""Almost a Circle Project"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Define a Class"""
    def __init__(self, size, x=0, y=0, id=None):
        self.__size = size
        self.__x = x
        self.__y = y
        super().__init__(id, size, x, y)

    def __str__(self):
        """__str__"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}")
