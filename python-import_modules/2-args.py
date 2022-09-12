#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
        print("1: {}".format(argv[1]))
    else:
        print(f"{argc} arguments:".format(argc))
        for i in range(1, argc + 1):
            print(f"{i}: {argv[i]}")
