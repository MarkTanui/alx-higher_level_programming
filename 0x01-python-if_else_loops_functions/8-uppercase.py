#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        print(chr(ord(str[i]) - 32), end='')

uppercase(str = "hello its me")