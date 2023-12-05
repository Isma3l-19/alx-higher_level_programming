#!/usr/bin/python3
"""defines file appending function"""
def append_write(filename="", text=""):
    """appends a string at the end of a UTF-8 file
    Args:
        filename (str):name of the file to be appended
        text (str): 
        string to append
    Returns:
        number of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
