#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
result = f"Last digit of {number} is {str(number)[-1]} "

last_digit = int(str(number)[-1])

if last_digit > 5:
    result += "and is greater than 5"
elif last_digit == 0:
    result += "and is 0"
elif last_digit < 6 and last_digit > 0:
    result += "and is less than 6 and not 0"

print(result)
