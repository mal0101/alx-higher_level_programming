#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for key, value in a_dictionary.items():
        new.update({key: (value * 2)})
    return new
