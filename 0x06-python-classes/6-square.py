#!/usr/bin/python3
""" This module contains the square class"""


class Square:
    """ represents a square class with instance private attribute - size"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

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

    @property
    def position(self):
        return _Square__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")

        x, y = value
        not_pos_ints = x < 0 and y < 0
        if (not isinstance(x, int) or not isinstance(y, int) or not_pos_ints):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._Square__position = (x, y)

    def area(self):
        return self._Square__size ** 2

    def my_print(self):
        if self._Square__size == 0:
            print("")
        else:
            i, j = 0, 0
            for i in range(self._Square__position[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(
                    " " * self._Square__position[0], "#" * self.__size))
