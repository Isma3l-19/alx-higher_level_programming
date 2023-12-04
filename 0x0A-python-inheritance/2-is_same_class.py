#!/usr/bin/python3
def is_same_class(obj, a_class):
    """checks if an object is an instance of a given class
    Args:
        obj (any): object to check
        a_class (type): class to match the type of obj yo
    Returns:
        True if obj is exactly an instance of a_class
        otherwise False
    """
    if type(obj) == a_class:
        return True
    return False
