#!/usr/bin/python3
"""Class MyList that inherits from list"""


class MyList(list):
    """Define a Class"""
    def print_sorted(self):
        print(sorted(self))
