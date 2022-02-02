# -*- coding: utf-8 -*-
import threading
import time

import schedule

from logHandler import logger
from crawl import Crawler


def run_thread(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


def __run_crawl():
    crawler = Crawler()
    crawler.run()


schedule.logger = logger
schedule.every(1).minutes.do(run_thread, __run_crawl)
schedule.run_all()
while True:
    schedule.run_pending()
    time.sleep(1)
