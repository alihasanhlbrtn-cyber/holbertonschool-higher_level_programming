#!/usr/bin/python3
"""Module that provides a lookup function for objects."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
