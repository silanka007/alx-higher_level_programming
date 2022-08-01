#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
    """
      MyList class that extends the inbuilt list object
    """

    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
