#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    import requests
    url = 'https://swapi.co/api/people/?search={}'.format(argv[1])
    r = requests.get(url).json()
    people = '\n'.join([person['name'] for person in r['results']])
    if r['count'] > 0:
        people = '\n' + people
    print('Number of result: {}{}'.format(r['count'], people))
    if r['next'] is not None:
        r = requests.get(r['next']).json()
        while r['next'] is not None:
            people = '\n'.join([person['name'] for person in r['results']])
            print(people)
            r = requests.get(r['next']).json()
        people = '\n'.join([person['name'] for person in r['results']])
        print(people)
