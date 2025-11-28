#!/usr/bin/python3
"""Module that defines inherits_from function."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a subclass of a_class.

    The object must be an instance of a class that inherited (directly or
    indirectly) from a_class, but not an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
