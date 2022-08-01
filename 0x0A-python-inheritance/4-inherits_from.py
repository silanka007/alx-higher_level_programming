#!/usr/bin/python3
""" module contains inherits_from function """


def inherits_from(obj, a_class):
    """
      checks if an obj inherits from a subclass
      that inherits from the specified class
    """
    return type(obj) != a_class and isinstance(obj, a_class)
