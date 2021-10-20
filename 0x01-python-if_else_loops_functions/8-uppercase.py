#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= 97 and ord(x) <= 122:
            n = chr(ord(x) - 32)
        else:
            n = x
        print(("{}").format(n), end="")
    print()
