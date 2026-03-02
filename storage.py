"""Storage module for TaskFlow - handle JSON data persistance.

This module provides functions to load and save tasks to a JSON file.
Using JSON makes our data human-readable and easy to debug.
"""

import json
from pathlib import Path

# Path to our data file
TASK_FILE = Path("tasks.json")

def load_tasks():
    """Load tasks from the JSON file.
    
    Returns:
        dict: Contains 'tasks' list and 'next_id' counter.
            Returns default structure if file doesn't exist.
    """
    
    if TASK_FILE.exists():
        with open(TASK_FILE, 'r') as f:
            return json.load(f)
    return {"tasks": [], "next_id": 1}

def save_tasks(data):
    """Save tasks to the JSON file.
    
    Args:
        data: Dictionary with 'tasks' list and 'next_id' counter.
    """
    with open(TASK_FILE, 'w') as f:
        json.dump(data, f, indent=2)