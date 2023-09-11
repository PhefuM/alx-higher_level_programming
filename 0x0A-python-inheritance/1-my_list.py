#!/usr/bin/python3
"""Contains a class definition which extends the list class
adding an instance method to produce a sorted replica of list
"""


class MyList(list):
    """a subclass of list"""

    def print_sorted(self):
        """prints the sorted ascending format of the list"""
        print(sorted(self))
