#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    i = 0
    for j in range(argc):
        i += int(argv[j + 1])
        print(i)
