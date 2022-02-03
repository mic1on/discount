# -*- coding: utf-8 -*-
from urllib.parse import urljoin, quote_plus

from spiders import Request


class Spiders(object):

    @staticmethod
    def guang_diu(word):
        url = f'https://guangdiu.com/search.php?q={quote_plus(word)}&keyfrom=hsearch'
        parser = Request().get(url).encode.parser
        a_lst = parser.xpath("//a[@class='goodname']")
        for a in a_lst:
            yield dict(title=a.xpath('./@title').get(),
                       href=urljoin(url, a.xpath('./@href').get()))

    @staticmethod
    def smzdm(word):
        url = f'https://search.smzdm.com/?c=faxian&s={quote_plus(word)}&v=b'
        parser = Request().get(url).encode.parser
        a_lst = parser.xpath("//a[@class='feed-nowrap']")
        for a in a_lst:
            yield dict(title=a.xpath('./@title').get(),
                       href=a.xpath('./@href').get())

    @staticmethod
    def ysj(word: str):
        """云神价"""
        url = f'http://www.yunshenjia.com/shenjia/search.html?keyword={quote_plus(word)}&min=&max='
        parser = Request().get(url).encode.parser
        a_lst = parser.xpath("//a[@class='preview']")
        for a in a_lst:
            title = a.xpath('./@title').get()
            # 这网站搜索出来的结果不精准
            words = word.split()
            for _word in words:
                if _word not in title:
                    return
            yield dict(title=title,
                       href=urljoin(url, a.xpath('./@href').get()))


if __name__ == '__main__':
    spider = Spiders()
    for _ in spider.guang_diu(""):
        print(_)
