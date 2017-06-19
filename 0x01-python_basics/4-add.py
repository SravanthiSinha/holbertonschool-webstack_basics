#!/usr/bin/python3
add = __import__("add_4").add


def addition():
    """calls the add function passing with the value of a and b"""
    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))

"""not executed when imported"""
if __name__ == "__main__":
    addition()
