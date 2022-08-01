#!/usr/bin/python3
""" This module contains the square class"""


class Square:
    """ represents a square class with instance private attribute - size"""

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self._Square__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self._Square__size = value

    def area(self):
        return self._Square__size ** 2

    def my_print(self):
        if self._Square__size == 0:
            print("")
        else:
            for i in range(self._Square__size):
                print(f"{'#' * self._Square__size}")
