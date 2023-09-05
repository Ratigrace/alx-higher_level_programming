#!/usr/bin/python3
"""Defining a locked class."""


class LockedClass:
    """
    Preventing user from dynamically creating new LockedClass
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
