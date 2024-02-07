#!/usr/bin/python3
"""load_from_json_file function"""

import json


def load_from_json_file(filename):
    """function that creates an Obj from JSON file with load not loads””"""
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
