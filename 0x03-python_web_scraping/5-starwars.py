#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    import requests
    url = 'https://swapi.co/api/people/?search={}'.format(argv[1])
    r = requests.get(url).json()
    people = '\n'.join(list(person['name'] for person in r['results']))
    if r['count'] > 0:
        people = '\n' + people
    print('Number of result: {}{}'.format(r['count'], people))
