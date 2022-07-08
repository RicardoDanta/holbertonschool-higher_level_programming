#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
ld = abs(number) % 10
if number < 0:
    ld = -ld
if ld > 5:
    print(f"Last digit of %d is {ld} and is greater than 5" % number)
elif ld == 0:
    print(f"Last digit of %d is {ld} and is 0" % number)
elif ld < 6 and number != 0:
    print(f"Last digit of %d is {ld} and is less than 6 and not 0" % number)
