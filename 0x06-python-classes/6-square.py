#!/usr/bin/python3
""" This module contains the square class"""


class Square:
    """ represents a square class with instance private attribute - size"""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if (type(value) != int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if (isinstance(value, tuple) and len(value) == 2):
            x, y = value
            if (isinstance(x, int) and isinstance(y, int)):
                if (x >= 0 and y >= 0):
                    self.__position = value
                else:
                    raise TypeError(
                        "position must be a tuple of 2 positive integers")
            else:
                raise TypeError(
                    "position must be a tuple of 2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            i, j = 0, 0
            for i in range(self.__position[1]):
                print()
            for j in range(self.__size):
                print("{}{}".format(
                    " " * self.__position[0], "#" * self.__size))


my_square = Square(3, (1, -3))
