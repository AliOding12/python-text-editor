import os
from tkinter import messagebox


def ask_yes_no(title, message):
    """Show a Yes/No message box and return True if 'Yes' was clicked."""
    return messagebox.askyesno(title, message)


def file_exists(path):
    """Check if a file exists."""
    return os.path.exists(path)


def read_file(path):
    """Read the contents of a file."""
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    """Write content to a file."""
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
# Add helper functions for utilities
# Add text formatting helpers
