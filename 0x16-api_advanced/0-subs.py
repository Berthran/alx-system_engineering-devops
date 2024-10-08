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
    try:
        url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
        headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0\
            (by /u/Large_Alternative_30)"
        }
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 404:
            return (0)
        results = response.json().get("data")
        return (results.get("subscribers"))
    except Exception:
        # print('Not Found')
        return (0)


# def main():
#     '''Calls the number_of_subscribers() function'''
#     subreddit = sys.argv[1]
#     number_of_subscribers(subreddit)


# if __name__ == '__main__':
#     main()
