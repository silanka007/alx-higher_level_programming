#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    res = []

    for i in range(2):
        first_val = tuple_a[i] if i <= len(tuple_a) - 1 else 0
        second_val = tuple_b[i] if i <= len(tuple_b) - 1 else 0
        res.append(first_val + second_val)

    return tuple(res)
