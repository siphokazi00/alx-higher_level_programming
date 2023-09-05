#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number % 10
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
if last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
if (not last_digit == 0) and last_digit < 6:
    str1 = "Last digit of"
    str2 = "and is less than 6 and not 0"
    print(f"{str1} {number} is {last_digit} {str2}")
