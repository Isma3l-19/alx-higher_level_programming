#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replace elements in a list like c"""
    if idx >= 0 and idx < len(my_list):
        my_list[idx] = element
    return (my_list)
