#!/usr/bin/python3
"""Write a function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """Say My Name"""
    if first_name is not str:
        raise TypeError("first_name must be a string")
    if last_name is not str:
        raise TypeError("last_name must be a string")
    print(f"My name is <first name> <last name>")
