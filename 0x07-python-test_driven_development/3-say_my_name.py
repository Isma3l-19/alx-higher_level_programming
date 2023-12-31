#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Args:
        first_name (str): first name to print
        last_name (str): last name to print
    Raises:
        TypeError: if neither first_name nor lst_name are strings
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
