#!/usr/bin/python3
'''Defining a text file reading function'''


def read_file(filename=""):
    '''Reading the contents of file UTF8 to stdout'''
    with open(filename, encoding="utf-8") as file:
        print(file.read(), end='')
