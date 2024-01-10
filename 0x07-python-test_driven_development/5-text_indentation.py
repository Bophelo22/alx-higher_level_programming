#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of these characters: ., ? and :"""
def text_indentation(text):
    """function that print a text"""
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    punc = text.replace('.', '.\n\n')
    punc = punc.replace('?', '?\n\n')
    punc = punc.replace(':', ':\n\n')
    newLine = punc.split('\n')
    for line in range(len(newLine)):
        print("{}".format(newLine[line].strip()),
              end=("" if (line == (len(newLine) - 1)) else '\n'))
