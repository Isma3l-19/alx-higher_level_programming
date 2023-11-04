#!/usr/bin/python3
"""Returns a tuple with the length of a string"""
def multiple_return(sentence):
     if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
