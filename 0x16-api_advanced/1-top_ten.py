#!/usr/bin/python3
'''
Gets the title of the first 10 hot posts listed for a given subreddit
'''


import requests
import sys


def main():
    '''Calls the top_ten function'''
    subreddit = sys.argv[1]
    top_ten(subreddit)


def top_ten(subreddit):
    '''
    Queries the reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit
    '''

    url = 'https://www.reddit.com/r/{}/hot.json?limit=9'.format(subreddit)
    response = requests.get(url, allow_redirects=False)
    if response.status_code != 200:
        print("None")
    else:
        children = response.json().get('data').get('children')
        for child in children:
            print(child.get('data').get('title'))


if __name__ == "__main__":
    main()
