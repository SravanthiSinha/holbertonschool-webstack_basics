#!/usr/bin/python3
if __name__ == "__main__":
    add = __import__('add-4').add
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
