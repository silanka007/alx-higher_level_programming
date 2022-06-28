#!/usr/bin/python3

def uppercase(str):
    result = ""
    for i in str:
        ascii_val = ord(i)
        if ascii_val in range(97, 123):
            result += chr(ascii_val - 32)
        else:
            result += i
    print("{}".format(result))
