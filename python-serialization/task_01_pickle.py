#!/usr/bin/env python3
"""Module for serializing and deserializing a custom class with pickle."""

import pickle


class CustomObject:
    """A custom object with basic attributes that can be pickled."""

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject instance."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file using pickle.

        Args:
            filename (str): The name of the file to save the object to.

        If any error occurs (e.g. invalid path), return None.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an instance of CustomObject from a file.

        Args:
            filename (str): The name of the file to load the object from.

        Returns:
            CustomObject or None: The loaded object if successful and of the
            correct type, otherwise None.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if not isinstance(obj, cls):
                return None
            return obj
        except Exception:
            return None
