#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv
    import requests
    url = 'https://api.github.com/repos/{}/{}/commits'\
        .format(argv[2], argv[1])
    r = requests.get(url)
    results = ''
    count = 0
    for commit in r.json():
        count += 1
        if count > 10:
            break
        results += '{}: {}\n'.format(commit['sha'],
                                     commit['commit']['author']['name'])
    print(results, end="")
