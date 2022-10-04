#!/usr/bin/python3
"""Almost a Circle Project"""


class Base():
    """Define a Class"""
    __nb_objects = 0
    

    def __init__(self, id=None):
    if type(id) is not None:
        self.id = id
    Base.__nb_objects += 1
