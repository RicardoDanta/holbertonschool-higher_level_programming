#!/usr/bin/python3
"""a function that creates an Object"""


def load_from_json_file(filename):
    """from a JSON file"""
    import json
    """JSON File"""
    with open(filename, encoding="utf-8") as f:
        return(json.loads(f.read()))
