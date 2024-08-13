#!/usr/bin/python3
'''
Queries the Reddit API and  returns the number of subscribers (not active
users, total subscribers) for a given subreddit. If an invalid subreddit
is given, the function  returns 0.
'''


import requests
import sys


def number_of_subscribers(subreddit):
    '''
    queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit.
    '''
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)
    subscribers = response.json().get('data', {}).get('subscribers', 0)
    return (subscribers)


def main():
    subreddit = sys.argv[1]
    number_of_subscribers(subreddit)


if __name__ == '__main__':
    main()  # 0
