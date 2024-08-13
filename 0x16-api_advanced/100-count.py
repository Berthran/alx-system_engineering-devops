#!/usr/bin/python3
'''
Counts the number of hot articles for a given subreddit
'''

import requests
import sys


def count_words(subreddit, word_list, after=None, word_count={}):
    '''
    Returns a list containing the titles of all hot
    articles
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
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        return None
    main_data = response.json()

    data = main_data.get("data")

    children = data.get("children")

    for child in children:
        title = child.get("data", {}).get("title").lower()
        for word in word_list:
            if word.lower() in title:
                word_count[word] = word_count.get(word, 0) + \
                                   title.count(word.lower())
        # for word in word_list:
        #     if word.lower() in title:
        #         if word.lower() in word_count:
        #             word_count[word] += 1
        #         else:
        #             word_count[word] = 1

    after = data.get("after")

    if after:
        return count_words(subreddit, word_list, after, word_count)
    else:
        sorted_counts = sorted(word_count.items(),
                               key=lambda x: x[1], reverse=True)
        for word, count in sorted_counts:
            print("{}: {}".format(word, count))


def main():
    subreddit = sys.argv[1]
    word_list = sys.argv[2:]
    count_words(subreddit, word_list)


if __name__ == "__main__":
    main()
