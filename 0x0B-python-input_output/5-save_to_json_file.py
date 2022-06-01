#!/usr/bin/python3
"""function that writes an Object to a text file"""


def save_to_json_file(my_obj, filename):
    """using a JSON representation"""
    import json
    """JSON"""
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
