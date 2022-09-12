#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = argv
    i = 0
    for j in range(1, len(argc)):
        i = i + int(argc[j])
        print("{}".format(i))
