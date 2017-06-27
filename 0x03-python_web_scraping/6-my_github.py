#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    import requests
    url = 'https://api.github.com/user'
    r = requests.get(url, auth=(argv[1], argv[2]))
    try:
        print(r.json()['id'])
    except:
        print(None)
