#!/usr/bin/python3
""" contains is_same_class function """


def is_same_class(obj, a_class):
    """ check if an object is an instance of a class
      Args:
        obj: the object
        a_class: the class
    """
    return type(obj) == a_class
