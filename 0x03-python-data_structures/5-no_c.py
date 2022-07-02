#!/usr/bin/python3

def no_c(my_string):
    if my_string is None:
        return None
    res = ""
    for i in my_string:
        if i not in ["c", "C"]:
            res += i
    return res
