#!/usr/bin/python3
import random


number = random.randint(-10000, 10000)
is_neg = number < 0
last_digit = int(str(number)[-1])
last_digit = last_digit if not is_neg else -1 * last_digit

result = f"Last digit of {number} is {last_digit} "

if last_digit > 5:
    result += "and is greater than 5"
elif last_digit == 0:
    result += "and is 0"
elif last_digit < 6 and last_digit != 0:
    result += "and is less than 6 and not 0"

print(result)
