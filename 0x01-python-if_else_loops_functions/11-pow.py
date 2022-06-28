#!/usr/bin/python3
import math


def pow(a, b):
    result = 1
    for i in range(b):
        result *= a

    return result


def pow2(a, b):
    return a ** b

