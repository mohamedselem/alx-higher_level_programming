#!/usr/bin/python3
"""Defines string to JSON FUnction."""
import json


def to_json_string(my_obj):
    """Return the JSON representation of a string OBJt."""
    return json.dumps(my_obj)
