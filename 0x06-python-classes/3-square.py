#!/usr/bin/python3
""" This module contains the square class"""


class Square:
    """ represents a square class with instance private attribute - size"""

    def __init__(self, size=0):
        if(type(size) != int):
            raise TypeError("size must be an integer")
        if(size < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = size

    def area(self):
        return self._Square__size ** 2
