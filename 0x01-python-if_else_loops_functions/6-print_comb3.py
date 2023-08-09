#!/usr/bin/python3
number = 0
while number <= 89:
    if number % 10 == 0 and number != 0:
        number += 1
        continue
        print("{:02d}".format(number), end='\n' if number == 89 else ", ")
        number += 1
