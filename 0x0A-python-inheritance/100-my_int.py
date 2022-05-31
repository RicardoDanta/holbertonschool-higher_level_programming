#!/usr/bin/python3
"""class MyInt"""


class MyInt(int):
    """inherits from int"""
    def __eq__(self, result):
        """False"""

        return False

    def __ne__(self, result):
        """True"""
        return True
