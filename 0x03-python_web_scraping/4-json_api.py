#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    import requests
    url = 'http://0.0.0.0:5000/search_user'
    data = {'q': ""}
    if len(argv) > 1:
        data['q'] = argv[1]
    r = requests.post(url, data=data)
    if r.text == '{}\n':
        print('No result')
    else:
        try:
            print('[{}] {}'.format(r.json()['id'], r.json()['name']))
        except ValueError:
            print('Not a valid JSON')
