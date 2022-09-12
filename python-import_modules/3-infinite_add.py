#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    args = argv
    i = 0
    
    for j in range(1, len(args)):
        i = i + int(args[j])
    print("{}".format(i))
