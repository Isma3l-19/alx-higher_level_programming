#!/usr/bin/python3
"""a program that prints alphabet, in lowercase, not followed by a new line."""
for letters in range(97, 123):
    print("{}".format(chr(letters)), end="")
