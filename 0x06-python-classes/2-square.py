#!/usr/bin/python3

""" clase """


class Square:
    """ inicializar """
    def __init__(self, size=0):
        """ asdf """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
