#!/usr/bin/python3
"""
Contains definition of the function lookup
"""


def lookup(obj):
    """
      returns a list of all available methods
      and attributes of an object

      @obj: an object
    """
    return dir(obj)
