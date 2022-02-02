# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor

from db.redisClient import db
from logHandler import logger
from notification import notify
from settings import SPIDERS, SEARCH_WORDS, MAX_WORKERS
from spiders import Spiders


def do(func):
    for word in SEARCH_WORDS:
        for item in func(word):
            href = item.get('href')
            title = item.get('title')
            if not href:
                continue
            if db.insert(href):
                notify.send_message(href, f"[优惠通知]{title}")


class Crawler(object):

    def run(self):
        spiders = SPIDERS
        func_list = []
        for spider in spiders:
            func = getattr(Spiders, spider, None)
            if not func:
                logger.error(f"class method Spider.{spider} not exists!")
                continue
            func_list.append(func)
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as t:
            t.map(do, func_list)


if __name__ == '__main__':
    crawler = Crawler()
    crawler.run()
