#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv)
    i = 0
    for j in range(1, argc):
        i += int(argv[j])
        print(i)
