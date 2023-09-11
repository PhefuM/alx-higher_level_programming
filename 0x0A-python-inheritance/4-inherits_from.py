#!/usr/bin/python3
"""
Contains the is_kind_of_class function
"""


def inherits_from(obj, a_class):
    """True if obj is an instance or inherited from a_class, else False"""
    return (isinstance(type(obj), a_class) and type(obj) != a_class)
