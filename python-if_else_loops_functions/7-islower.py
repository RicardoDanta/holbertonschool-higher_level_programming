#!/usr/bin/python3
def islower(c):
    l = ord(c)
    for i in range(97, 122):
        if i == l:
            return True
        return False
