#!/usr/bin/python3
"""Reddit API recursive function"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """Queries Reddit API returns list of titles of all hot articles"""
    url = "https://www.reddit.com/r/{}/hot.json?after={}".format(subreddit, after)
    headers = {"User-Agent": "linux:0.0.1 (by /u/nameofuser)"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    if response.status_code != 200:
        return None

    after = response.json().get("data").get("after")
    posts = response.json().get("data").get("children")

    for post in posts:
        hot_list.append(post.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after)
    return hot_list
