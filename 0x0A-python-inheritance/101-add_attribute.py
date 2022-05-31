#!/usr/bin/python3
""" def add_attribute """


def add_attribute(objet, att_name, att_value):
    """def add"""

    if not hasattr(objet, "__dict__"):
        raise TypeError("can't add new attribute")
    else:
        setattr(objet, att_name, att_value)
