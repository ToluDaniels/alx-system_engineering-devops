#!/usr/bin/python3
"""
Returns all the data for a given subreddit recursively.


"""
import requests


def recurse(subreddit, hot_list=[]):
    """
    Implementation. 
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()['data']['children']
        for post in data:
            hot_list.append(post['data']['title'])
        if data:
            return recurse(subreddit, hot_list=hot_list+data)
    elif response.status_code == 404:
        return None
    else:
        return None
