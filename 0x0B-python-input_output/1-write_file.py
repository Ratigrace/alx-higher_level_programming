#!/usr/bin/python3
'''Defing a function that writes to txt file UTF8'''


def write_file(filename="", text=""):
    '''Writing a string to a txt file

    Args:
        filename: The name of file to write
        text: the string to write to file
    Returns:
        The number of characters written
        '''
    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
