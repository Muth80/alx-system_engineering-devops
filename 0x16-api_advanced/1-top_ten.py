#!/usr/bin/python3
"""
Fetch top 10 hot post titles from a subreddit
"""
import requests


def top_ten(subreddit):
    """Prints titles of top 10 hot posts for a given subreddit"""
    base_url = 'https://www.reddit.com/'
    headers = {'user-agent': 'my-app/0.0.1'}
    response = requests.get(base_url + 'r/' + subreddit + '/hot.json',
                            headers=headers, allow_redirects=False)
    if response.status_code == 200:
        posts = response.json().get('data').get('children')
        for post in posts[:10]:
            print(post.get('data').get('title'))
    else:
        print(None)
