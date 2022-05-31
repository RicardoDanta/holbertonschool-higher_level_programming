#!/usr/bin/python3
"""function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """and returns the number of characters added"""
    with open(filename, mode="a", encoding="utf-8") as f:
        """Append"""
        return f.write(text)
