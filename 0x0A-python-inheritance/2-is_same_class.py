#!/usr/bin/python3
"""
returns True if the object is exactly an instance of the specified class,otherwise False
"""


def is_same_class(obj, a_class):
    """
    checks if an object is an instance of class
    """
    if(isinstance(obj, a_class) == True):
        return True
    else:
        return False
