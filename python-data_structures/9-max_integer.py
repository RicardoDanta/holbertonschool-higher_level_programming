#!/usr/bin/python3
def max_integer(my_list=[]):
    for i in range(len(my_list)):
        if my_list[i] > my_list[0]:
            my_list = my_list[i]
            return my_list
