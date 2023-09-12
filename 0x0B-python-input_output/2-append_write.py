#!/usr/bin/python3
"""Defining a function to apend sring."""


def append_write(filename="", text=""):
    """Appending a string to the end of a UTF8 text file.

    Args:
        filename: The name of the file to append to.
        text: The string to append to the file.
    Returns:
        The number of characters appended.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
