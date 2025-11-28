#!/usr/bin/python3
"""Module that provides class_to_json function."""


def class_to_json(obj):
    """Return the dictionary description of an object's attributes.

    The dictionary contains only simple data structures suitable
    for JSON serialization (lists, dicts, strings, ints, bools).
    """
    return obj.__dict__
