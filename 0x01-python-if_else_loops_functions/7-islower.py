#!/usr/bin/python3

def islower(c):
    asci_val = ord(c)
    if asci_val in range(97, 123):
        return True
    return False
