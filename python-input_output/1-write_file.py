#!/usr/bin/python3
"""Module that defines a function to write text to a file."""


def write_file(filename="", text=""):
    """Write a string to a UTF-8 text file and return the number of characters."""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
