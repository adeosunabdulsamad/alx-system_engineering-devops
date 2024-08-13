#!/usr/bin/python3
"""Module to query the Reddit API and returns the number of subscribers"""
import requests

def number_of_subscribers(subreddit):
    """Returns the number of subscribers for a given subreddit"""
    headers = {'User-Agent': 'MyRedditAPI/0.1 by YourUsername'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers, allow_redirects=False)
                
    if response.status_code == 200 and 'data' in response.json():
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0
