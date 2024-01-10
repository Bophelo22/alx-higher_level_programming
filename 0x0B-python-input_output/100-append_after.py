#!/usr/bin/python3
"""
function that inserts a line of text to a file, after each line containing
a specific string (see example):
"""
def append_after(filename="", search_string="", new_string=""):
    """appends str after lines that include keyword (search_string)
    """
    with open(filename, mode="r+", encoding="utf-8") as file:
        new_text = ""
        for line in file:
            new_text += line
            if search_string in line:
                new_text += new_string
        file.seek(0)
        file.write(new_text)
