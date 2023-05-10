#!/usr/bin/python3
"""
Counts.


"""
import requests

def count_words(subreddit, word_list, count_dict=None):
    """
    Implementation.
    """
    # Initialize the count dictionary if it hasn't been created yet
    if count_dict is None:
        count_dict = {}

    # Query the Reddit API for the hot posts in the subreddit
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    # If the subreddit is invalid, return nothing
    if response.status_code != 200:
        return

    # Parse the titles of the hot posts and count the occurrences of the given keywords
    data = response.json()
    for post in data["data"]["children"]:
        title = post["data"]["title"].lower()
        for word in word_list:
            if word.lower() in title:
                count_dict[word] = count_dict.get(word, 0) + title.count(word.lower())

    # Recursively call the function on the next page of results, if there is one
    if data["data"]["after"] is not None:
        count_words(subreddit, word_list, count_dict=count_dict)

    # Sort and print the results
    sorted_counts = sorted(count_dict.items(), key=lambda x: (-x[1], x[0]))
    for word, count in sorted_counts:
        print(f"{word}: {count}")
