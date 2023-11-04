#!/usr/bin/python3
"""Retrieves elements from a list like in c"""
def element_at(my_list, idx):
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    return (my_list[idx])
