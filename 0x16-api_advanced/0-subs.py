#!/usr/bin/python3
""" Return number of All subscribers"""

import requests


def number_of_subscribers(subreddit):
    """Get All subscribers number for a given subreddit"""

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {'User-Agent': 'AyaTarek95'}
    res = requests.get(url, headers=headers)

    if res.status_code == 200:
        data = res.json()
        subscribers_num = data['data']['subscribers']
        return subscribers_num

    else:
        return 0
