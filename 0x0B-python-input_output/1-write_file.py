#!/usr/bin/python3
"""function that writes a string to a text file"""


def write_file(filename="", text=""):
    """and returns the number of characters written"""

    with open(filename, mode="w", encoding="UTF-8") as f:
        return(f.write(text))
