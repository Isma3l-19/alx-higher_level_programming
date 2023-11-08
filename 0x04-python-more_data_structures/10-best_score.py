#!/usr/bin/python3
def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    tom = list(a_dictionary.keys())[0]
    boy = a_dictionary[tom]
    for i, j in a_dictionary.items():
        if v > big:
            boy = j
            tom = i
    return (tom)
