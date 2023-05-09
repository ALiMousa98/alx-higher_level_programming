#!/usr/bin/python3
def uppercase(str):
    for c in str:
        if ord(c) in range(ord('a'), ord('z')+1):
            print("{}".format(chr(ord(c) - 32)), end='')
        else:
            print("{}".format(c), end='')
    print("")
