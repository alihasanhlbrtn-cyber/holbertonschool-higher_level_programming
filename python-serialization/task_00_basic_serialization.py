#!/usr/bin/env python3
"""
Basic serialization module.

Provides functions to:
- serialize a Python dictionary to a JSON file
- deserialize a JSON file back into a Python dictionary
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to a file.

    Args:
        data (dict): The dictionary to serialize.
        filename (str): The name of the output JSON file.
                        If it exists, it will be overwritten.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load JSON data from a file and deserialize it into a Python dictionary.

    Args:
        filename (str): The name of the input JSON file.

    Returns:
        dict: The deserialized dictionary.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
