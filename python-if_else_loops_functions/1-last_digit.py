#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if ld > 5:
    print(f"Last digit of {number} is {ld} and is grater than 5" % number)
if ld == 0:
    print(f"Last digit of {number} is {ld} and is 0" % number)
if ld < 6 and is not 0:
    print(f"Last digit of {number} is {ld} and is less than 6 and not 0" % number)
