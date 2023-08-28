#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        print()  # Print a new line
        return True
    except:
        error_message = "Exception: Unable to print value as an integer"
        print(error_message, file=sys.stderr)
        return False
