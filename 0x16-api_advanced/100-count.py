#!/usr/bin/python3
"""Module that prints list of posts listed for a given subreddit"""
import requests

def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API, parses the titles of all hot articles,
    and counts the occurrences of given keywords in a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to search.
        word_list (list of str): A list of keywords to count.
        after (str, optional): The 'after' parameter for pagination. Defaults to None.
        word_count (dict, optional): A dictionary storing the count of keywords. Defaults to {}.

    Returns:
        None: Prints the sorted count of keywords. If the subreddit is invalid, prints nothing.
    """
    headers = {'User-Agent': 'My-User-Agent'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code != 200:
        return

    data = response.json().get('data', {})
    children = data.get('children', [])
    after = data.get('after')

    if not word_count:
        word_count = {word.lower(): 0 for word in word_list}

    for post in children:
        title = post.get('data', {}).get('title', '').lower()
        words_in_title = title.split()
        for word in words_in_title:
            cleaned_word = ''.join(char for char in word if char.isalnum())
            if cleaned_word in word_count:
                word_count[cleaned_word] += 1

    if after:
        return count_words(subreddit, word_list, after, word_count)
    else:
        sorted_word_count = sorted(
            [(word, count) for word, count in word_count.items() if count > 0],
            key=lambda item: (-item[1], item[0])
        )

        for word, count in sorted_word_count:
            print(f"{word}: {count}")
