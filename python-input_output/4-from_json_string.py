#!/usr/bin/python3
"""Function that returns an object (Python data structure)
represented by a JSON string"""
import json


def from_json_string(my_str):
    """Return an Object"""
    return json.loads(my_str)
