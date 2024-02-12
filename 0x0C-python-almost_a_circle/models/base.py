#!/usr/bin/python3
"""models/base.py"""
import json


class Base:
    """A representation of the base of our OOP hierarchy"""

    __nb__objects = 0

    def __init(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base._nb_objects += 1
            self.id = Base.__nb_objects
