#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
    
    Returns:
        int: The number of subscribers for the subreddit. Returns 0 if the subreddit
             is invalid or any error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'my-app/0.0.1'}
    
    try:
        # Make the GET request
        response = requests.get(url, headers=headers, allow_redirects=False)
        
        # Check if the subreddit is valid
        if response.status_code == 200:
            data = response.json()
            return data['data']['subscribers']
        else:
            return 0
    except Exception as e:
        return 0

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        print("{:d}".format(number_of_subscribers(sys.argv[1])))
