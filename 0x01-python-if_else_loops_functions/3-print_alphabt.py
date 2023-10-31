#!/usr/bin/python3
"""Program that prints alphabets in lowercase"""
for letters in range(97, 123):
    if letters != 101 and letters != 113:
        print("{}".format(chr(letters)), end="")
