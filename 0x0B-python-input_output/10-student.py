#!/usr/bin/python3
"""Defines class Student."""


class Student:
    def __init__(self, first_name, last_name, age):
        """Reps a student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dict rep of Student"""

        if attrs is None:
            return self.__dict__
        else:
            valid_attrs = {}
            for attr in attrs:
                if hasattr(self, attr):
                    valid_attrs[attr] = getattr(self, attr)
            return valid_attrs
