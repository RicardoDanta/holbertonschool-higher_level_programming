#!/usr/bin/python3
"""class MyList"""


class MyList(list):
    """inherits from list"""
    def print_sorted(self):
        """Print"""
        print(sorted(self))
