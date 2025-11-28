#!/usr/bin/env python3
"""
Convert CSV data to JSON and save it to data.json.
"""

import csv
import json


def convert_csv_to_json(filename):
    """Convert a CSV file to JSON and save as data.json.

    Args:
        filename (str): Path to the input CSV file.

    Returns:
        bool: True if conversion succeeded, False otherwise.
    """
    try:
        # Read CSV into a list of dictionaries
        with open(filename, mode="r", encoding="utf-8", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            rows = list(reader)

        # Write JSON to data.json
        with open("data.json", mode="w", encoding="utf-8") as json_file:
            json.dump(rows, json_file)

        return True
    except Exception:
        # Any error (e.g., file not found) -> return False
        return False
