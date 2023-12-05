#!/usr/bin/python3

"""defines a JSON-to-object function"""
import json


def from_json_string(my_str):
    """returns the converted string"""
    return json.loads(my_str)
