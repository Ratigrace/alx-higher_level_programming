#!/usr/bin/python3

def uniq_add(my_list=[]):
    # Create a set to keep track of unique integers
    unique_integers = set()

    # Iterate through the elements in the input list
    for num in my_list:
        unique_integers.add(num)

    # Sum up the unique integers in the set and return the result
    total = sum(unique_integers)
    return total
