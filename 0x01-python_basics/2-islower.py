#!/usr/bin/python3
def islower(c):
    for x in c:
        if ord(x) < 97 or ord(x) > 122:
            return False
    return True
