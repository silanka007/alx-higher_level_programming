#!/usr/bin/python3
""" module contains is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """ returns true if an object is an instance of a class
      else false
      Args:
        obj: an obj
        a_class: a class
    """
    return isinstance(obj, a_class)
