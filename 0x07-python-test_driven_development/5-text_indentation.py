#!/usr/bin/python3
"""Define text_indentation function"""


def text_indentation(text):
    """prints a text with 2 new lines after characters: ., ? and':'."""
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.replace("? ", "?\n\n")
    text = text.replace(":    ", ":\n\n")
    text = text.replace(": ", ":\n\n")
    text = text.replace(". " or ".", ".\n\n")
    print(text, end="")
