#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """Prints a dictionary by ordered keys"""
    [print("{}: {}".format(i, a_dictionary[k])) for i in sorted(a_dictionary)]
