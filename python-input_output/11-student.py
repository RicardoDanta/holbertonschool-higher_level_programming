#!/usr/bin/python3
"""class Student that defines a student"""


class Student():
    """Define a Class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Def to json"""
        if attrs is None:
            return self.__dict__
        dictionary = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                dictionary[key] = value
        return dictionary

    def reload_from_json(self, json):
        """Reload from JSON"""
        for key, value in json.items():
            setattr(self, key, value)
