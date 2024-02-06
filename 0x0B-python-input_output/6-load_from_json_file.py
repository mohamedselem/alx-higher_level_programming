#!/usr/bin/python3
"""Defines  JSON file Reading function."""
import json


def load_from_json_file(filename):
    """Create a Python object from JSON file."""
    with open(filename) as f:
        return json.load(f)
