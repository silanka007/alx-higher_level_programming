#!/usr/bin/python3
from calculator_1 import add, sub
import dis


def magic_calculation(a, b):
    if a < b:
        c = add(a, b)
        for i in range(4, 6):
            c += i
        return c
    else:
        return sub(a, b)
        return


print(dis.dis(magic_calculation))
