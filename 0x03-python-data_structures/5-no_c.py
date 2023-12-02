#!/usr/bin/python3

def no_c(my_string):
    results = ""
    for i in my_string:
        if i != 'c' and i !='C':
            results += i
    return results
