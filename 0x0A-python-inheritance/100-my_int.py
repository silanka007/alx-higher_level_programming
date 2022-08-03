#!/usr/bin/python3
"""contains MyInt class"""


class MyInt(int):
    """MyInt class inherits th built-in int class"""

    def __eq__(self, value):
        """overriding the default behavior to !="""
        return self.real != value

    def __ne__(self, value):
        """overriding the default behavior to =="""
        return self.real == value
