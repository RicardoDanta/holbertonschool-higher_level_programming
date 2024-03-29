#!/usr/bin/python3
"""Function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """Read a text file"""
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")
