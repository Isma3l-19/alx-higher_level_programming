#!/usr/bin/python3
def print_square(size):
    """prints a square with # character
    Args:
        size (int): height and width of the square
    Raises:
        TypeError: if size is not a integer
        ValueError: if size < 0
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be>= 0")

    for i in range(size):
        [print("#", end="") for x in range(size)]
        print("")
