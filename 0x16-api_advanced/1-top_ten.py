#!/usr/bin/python3
"""Module that prints title hot posts listed for a given subreddit"""
import requests


def top_ten(subreddit):
    """Returns the titles of hot posts listed for a given subreddit"""
    headers = {'User-Agent': 'MyRedditAPI/0.1 by YourUsername'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code >= 300:
        print(None)
        return

    data = response.json()
    posts = data.get('data', {}).get('children', [])
    for post in posts[:10]:
        print(post.get('data', {}).get('title', ''))
