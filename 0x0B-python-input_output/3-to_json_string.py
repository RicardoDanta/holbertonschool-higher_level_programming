#!/usr/bin/python3
"""function that returns the JSON representation"""


def to_json_string(my_obj):
    """of an object (string)"""
    import json
    """JSON"""
    return json.dumps(my_obj)
