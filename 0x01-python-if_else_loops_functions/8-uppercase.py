#!/usr/bin/python3
def uppercase(str):
    for ascii in str:
        if ((ord(ascii) >= ord('a')) and (ord(ascii) <= ord('z'))):
            #convert the letters to uppercase
            uppercase_lettr = chr(ord(ascii) - ord('a') + ord('A'))
            print(uppercase_lettr,end='')
        else:
            print(ascii,end='')
    print()
