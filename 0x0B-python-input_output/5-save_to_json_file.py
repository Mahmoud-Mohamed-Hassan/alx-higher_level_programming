#!/usr/bin/python3
"""save_to_json_file function"""

import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to created txt file,
    using a JSON representation"""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(my_obj, file)
