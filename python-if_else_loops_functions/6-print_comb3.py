#!/usr/bin/python3
for i in range(0, 10):
    for j in range(i, 10):
        if i != j and j == 9 and i + 1 == j:
            print("{:d}{:d}".format(i, j))
        elif i != j:
            print("{}{}".format(i, j), end=", ")
