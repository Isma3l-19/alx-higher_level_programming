#!/usr/bin/python3
class MyList(list):
    """implements sorted printing for the built-in list class""" 
    def print_sorted(self):
        """prints list in ascending order"""
        print(sorted(self))
