#!/usr/bin/python3
"""Write a function that prints a square with the character #"""


def print_square(size):
    """Define a Square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
