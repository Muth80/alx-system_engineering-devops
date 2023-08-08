#!/usr/bin/python3
"""
Module to count words
"""
import requests

def count_words(subreddit, word_list, after="", word_dict={}):
    """
    Recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints
    a sorted count of given keywords
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'My User Agent'}
    params = {'limit': 100, 'after': after}
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code != 200:
        return None
    next_page = response.json().get('data').get('after')
    if next_page is not None:
        count_words(subreddit, word_list, next_page, word_dict)
    hot_list = response.json().get('data').get('children')
    for word in word_list:
        for post in hot_list:
            title = post.get('data').get('title').lower().split()
            for title_word in title:
                if title_word == word.lower():
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
    if next_page is None:
        if bool(word_dict):
            sorted_tuple_list = sorted(word_dict.items(), key=lambda x: x[0])
            sorted_tuple_list.sort(key=lambda x: x[1], reverse=True)
            for key, value in sorted_tuple_list:
                print("{}: {}".format(key.lower(), value))
