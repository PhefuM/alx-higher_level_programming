#!/usr/bin/python3
"""This module defines a string-to-JSON function"""
inport json


def to_json_string(my_obj):
    """Returns the JSON representation of a string object"""
    return json.dumps(my_obj)
