#!/usr/bin/python3
"""
Returns the count for a given subreddit.


"""
import requests


def number_of_subscribers(subreddit):
    """
    Implementation for the function.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()['data']
        return data['subscribers']
    else:
        return 0
