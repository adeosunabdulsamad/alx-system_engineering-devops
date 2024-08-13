#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    headers = {'User-Agent': 'MyRedditAPI/0.1 by YourUsername'}
    response = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json', headers=headers, allow_redirects=False)
                
    if response.status_code == 200 and 'data' in response.json():
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0
