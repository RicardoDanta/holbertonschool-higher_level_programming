#!/usr/bin/python3
def no_c(my_string):
    char = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            char = char + i
    return char
