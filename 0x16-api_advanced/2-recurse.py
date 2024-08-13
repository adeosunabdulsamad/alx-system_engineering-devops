#!/usr/bin/python3
"""Module that prints list of posts listed for a given subreddit"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API and returns a list of hot articles
    in a given subreddit. If no results are found or the s.
    """
    h = {'User-Agent': 'My-User-Agent'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    p = {'limit': 100, 'after': after}
    response = requests.get(url, headers=h, params=p, allow_redirects=False)

    # Check for a valid response
    if response.status_code != 200:
        return None

    data = response.json().get('data', {})
    children = data.get('children', [])
    after = data.get('after')

    # Append titles to the hot_lis
    for post in children:
        hot_list.append(post.get('data', {}).get('title', ''))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
