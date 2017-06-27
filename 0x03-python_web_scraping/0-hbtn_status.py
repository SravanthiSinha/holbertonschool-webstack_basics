#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    import requests
    url = "https://intranet.hbtn.io/status"
    r = requests.get(url)
    print("Body response:")
    print("\t- type: {}\n\t- content: {}".format(type(r.text), r.text))
