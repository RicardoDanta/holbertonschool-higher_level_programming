#!/usr/bin/python3
"""function that adds a new attribute"""


def add_attribute(objet, att_name, att_value):
    """to an object if it’s possible"""

    if not hasattr(objet, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(objet, att_name, att_value)
