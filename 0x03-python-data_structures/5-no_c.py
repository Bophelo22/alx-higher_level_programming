#!/usr/bin/python3

def no_c(my_string):
    results = ""
    for i in my_string:
        if i != 'c' or i !='C':
            results += i
    return results
