#!/usr/bin/python3
"""Function that returns True if the object
is an instance of a class that inherited from the specified class,
otherwise False"""


def inherits_from(obj, a_class):
    """True or False"""
    return isinstance(obj, a_class)
