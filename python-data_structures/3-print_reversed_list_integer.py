#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    a = my_list[::-1]
    for i in a:
        print("{:d}".format(i, end="\n"))
