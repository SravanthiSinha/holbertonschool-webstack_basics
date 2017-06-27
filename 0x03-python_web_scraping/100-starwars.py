#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    import requests
    url = 'https://swapi.co/api/people/?search={}'.format(argv[1])
    r = requests.get(url).json()
    people = []
    for person in r['results']:
        person_films = '\n\t'.join([requests.get(film).json()['title']
                                    for film in person['films']])
        people.append('{}\n\t{}'.format(person['name'], person_films))
    people = '\n'.join(people)
    if r['count'] > 0:
        people = '\n' + people
    print('Number of result: {}{}'.format(r['count'], people))
    if r['next'] is not None:
        r = requests.get(r['next']).json()
        while r['next'] is not None:
            people = []
            for person in r['results']:
                person_films = '\n\t'.join([requests.get(film).json()['title']
                                            for film in person['films']])
                people.append('{}\n\t{}'.format(person['name'], person_films))
            people = '\n'.join(people)
            print(people)
            r = requests.get(r['next']).json()
        people = []
        for person in r['results']:
            person_films = '\n\t'.join([requests.get(film).json()['title']
                                        for film in person['films']])
            people.append('{}\n\t{}'.format(person['name'], person_films))
        people = '\n'.join(people)
        print(people)
