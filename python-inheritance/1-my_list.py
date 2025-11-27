#!/usr/bin/python3
"""Module that defines a custom list class MyList."""


class MyList(list):
    """A list that can print itself sorted."""

    def print_sorted(self):
        """Print the list in ascending sorted order (without modifying it)."""
        print(sorted(self))
