#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    lists = my_list.copy()
    for i in my_list:
        if idx < 0:
           return lists
        elif idx >= len(my_list):
           return lists
        else:
            lists[idx] = element
            return lists
