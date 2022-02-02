# -*- coding: utf-8 -*-
import random

import requests
import parsel


class Request(object):

    def __init__(self):
        self.response = None

    """请求"""

    @property
    def user_agent(self):
        user_agent_lst = [
            "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:22.0) Gecko/20130328 Firefox/22.0",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:24.0) Gecko/20100101 Firefox/24.0",
            "Opera/9.80 (X11; Linux i686; U; hu) Presto/2.9.168 Version/11.50",
            "Opera/9.80 (Windows NT 6.0; U; pl) Presto/2.10.229 Version/11.62",
            "Opera/9.80 (X11; Linux x86_64; U; pl) Presto/2.7.62 Version/11.00",
            "Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/4E423F",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
        ]
        return random.choice(user_agent_lst)

    @property
    def headers(self):
        return {
            "User-Agent": self.user_agent
        }

    def get(self, url, headers=None, timeout=10, *args, **kwargs):
        if headers is None:
            headers = {}
        headers.update(self.headers)
        self.response = requests.get(url=url, headers=headers, timeout=timeout, *args, **kwargs)
        return self

    @property
    def encode(self):
        self.response.encoding = self.response.apparent_encoding
        return self

    @property
    def text(self):
        return self.response.text

    @property
    def parser(self):
        return parsel.Selector(self.text)


from spiders.spiders import Spiders
