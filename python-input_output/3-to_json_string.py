#!/usr/bin/python3
"""Module that defines a function to get JSON representation of an object."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of an object (string)."""
    return json.dumps(my_obj)
