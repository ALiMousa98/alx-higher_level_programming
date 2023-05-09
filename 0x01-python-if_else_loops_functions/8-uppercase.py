#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            uppercase_c = chr(ord(c) - 32)
        else:
            uppercase_c = c
        print(uppercase_c, end='')
    print()
