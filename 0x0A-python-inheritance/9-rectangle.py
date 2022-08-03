#!/usr/bin/python3
""" module contains the Rectangle class"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ A Rectangle class"""

    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"

    def area(self):
        return self.__width * self.__height
