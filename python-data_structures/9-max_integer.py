#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == []:
        return None
    number = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > number:
            number = my_list[i]
    return number
