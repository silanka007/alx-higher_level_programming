#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    max_num = float("-inf")
    for num in my_list:
        if num > max_num:
            max_num = num
    return max_num
