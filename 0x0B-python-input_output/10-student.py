#!/usr/bin/python3
"""This module defines a class Student"""


class Student:
    """Represents a student"""

    def __init__(self, first_name, last_name, age):
        """Initializes a new Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Get a dictionary representation of a Student
        If attrs is a list of strings, represent only attributes in the list
        """
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) ofr k in attrs if hasattr(self, k)}
        return self.__dict__
