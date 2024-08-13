#!/usr/bin/python3
'''
Gets the title of the first 10 hot posts listed for a given subreddit
'''

import requests
import sys


def top_ten(subreddit):
    '''
    Queries the reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit
    '''
    if not subreddit:
        return

    headers = {'User-Agent': 'Mozilla/5.0'}

    params = {'limit': 10}

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print("None")
    else:
        main_data = response.json()
        data = main_data.get('data')
        children = data.get('children')

        for child in children:
            print(child.get('data').get('title'))


def main():
    '''Calls the top_ten function'''
    subreddit = sys.argv[1]
    top_ten(subreddit)


if __name__ == "__main__":
    main()
