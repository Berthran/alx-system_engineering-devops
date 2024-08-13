#!/usr/bin/python3
'''
Stores the titles of all hot articles for a given subreddit
'''
# Check 1: File exist
# Check 2: Shebang
# Check 3: Pycodestyle
# Check 4: Module doc

import requests
import sys


def recurse(subreddit, after=None, hot_list=[]):
    '''
    Returns a list containing the titles of all hot articles
    '''
    if not subreddit:
        return

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    headers = {"User-Agent": "Mozilla/5.0"}

    params = {}

    if after:
        params['after'] = after

    response = requests.get(url,
                            headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None
    main_data = response.json()

    data = main_data.get("data")

    children = data.get("children")

    for child in children:
        hot_list.append(child.get("data", {}).get("title"))

    after = data.get("after")

    if after:
        return recurse(subreddit, after, hot_list)
    return hot_list


def main():
    subreddit = sys.argv[1]
    recurse(subreddit)


if __name__ == "__main__":
    main()
