#!/usr/bin/python3
"""good job girl"""


def append_write(filename="", text=""):
    """append to a file"""
    with open(filename, 'a', encoding="utf-8") as fd:
        return fd.write(text)
