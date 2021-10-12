#!/usr/bin/python3
"""a function that appends a string at the end of a file"""


def append_write(filename="", text=""):
    """appends a string to a text file,returns the no of characters added"""
    with open(filename, mode='a') as f:
        f.write(text)
