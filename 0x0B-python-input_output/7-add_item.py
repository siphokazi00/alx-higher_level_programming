#!/usr/bin/python3
"""Defines a script that adds all args to a py list"""
import sys
import os

# Import functions
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Check if JSON file already exists
json_filename = 'add_item.json'
data = []

# Load JSON file if it exists
if os.path.exists(json_filename):
    data = load_from_json_file(json_filename)

# Append command-line arguments to list
data.extend(sys.argv[1:])

# Save updated list to JSON file
save_to_json_file(data, json_filename)

# Print list
print(data)
