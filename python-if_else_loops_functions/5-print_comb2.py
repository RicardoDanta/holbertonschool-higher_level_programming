#!/usr/bin/python3
number = 0
for number in range(0, 100):
    if number == 99:
        print(number)
        break
    print("{:02d}, ".format(number), end="")
