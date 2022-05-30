#!/usr/bin/python3
"""a function that returns True if the object is an instance"""


def is_same_class(obj, a_class):
    """otherwise False"""
    if type(obj) == a_class:
        return True
    return False
