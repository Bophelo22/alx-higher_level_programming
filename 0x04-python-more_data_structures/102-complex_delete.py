#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    new_list = []
    for i, j in a_dictionary.items():
        if value is j:
            new_list.append(i)
    if len(new_list) > 0:
        for k in new_list:
            del a_dictionary[k]
    return (a_dictionary)
