#!/usr/bin/python3

def uniq_add(my_list=[]):
    uniq = list(set(my_list))
    result = 0
    for num in uniq:
        result += num
    return result
