#!/usr/bin/python3
"""function that returns an object"""


def from_json_string(my_str):
    """represented by a JSON string"""
    import json
    """JSON STR"""
    return json.loads(my_str)

