#!/usr/bin/python3
"""
Prints title of the first 10 hotspots for a given reddit.
Pagination.

"""
import requests


def top_ten(subreddit):
    """
    Implementation.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']['children']
        for i in range(10):
            print(data[i]['data']['title'])
    else:
        print(None)
