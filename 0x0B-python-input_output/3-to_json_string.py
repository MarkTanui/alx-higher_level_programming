#!/usr/bin/python3
import json
"""a function that returns JSON represenatation"""


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    return json.dumps(my_obj)
