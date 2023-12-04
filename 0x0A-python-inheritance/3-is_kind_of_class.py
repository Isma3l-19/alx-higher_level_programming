#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """checks if an object is an instance or inheritance of class
    Args:
        obj (any): object to check
        a_class (type): class to match obj to
    Returns:
        True if obj is an instance or inheritace of a_class
        otherise False
    """
    if isinstance(obj, a_class):
        return True
    return False
