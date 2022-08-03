#!/usr/bin/python3
"""this module contains the Square class"""

Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """the Square class"""

    def __init__(self, size):
        self.__size = self.integer_validator("size", size)
        super().__init__(size, size)

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"

    def area(self):
        """calculate the area of an object instance"""
        return self.__size ** 2
