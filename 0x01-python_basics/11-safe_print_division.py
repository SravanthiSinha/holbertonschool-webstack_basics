#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = a / b
        print("Inside result: {:.1f}".format(res))