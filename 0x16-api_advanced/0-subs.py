#!/usr/bin/python3
"""Module to query the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    headers = {'User-Agent': 'MyRedditAPI/0.1 by YourUsername'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code < 300 and 'data' in response.json():
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0
