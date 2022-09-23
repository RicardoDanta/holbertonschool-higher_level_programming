#!/usr/bin/python3
"""Write a function that prints a text
with 2 new lines after each of the characters"""


def text_indentation(text):
    """Text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for delim in ".:?":
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])
    print("{}".format(text), end="")
