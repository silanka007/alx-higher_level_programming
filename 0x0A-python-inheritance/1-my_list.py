#!/usr/bin/python3
"""
Module: 1-my_list
"""


class MyList(list):
    """
      MyList class that extends the inbuilt list object
    """

    def print_sorted(self):
        """
        Prints list elements(int) in ascending order
        """
        print(sorted(self))


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod()
