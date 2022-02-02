# -*- coding: utf-8 -*-
from redis import Redis
from redis.connection import BlockingConnectionPool

from settings import REDIS_CONN


class RedisClient(object):

    def __init__(self, url, **kwargs):
        self.name = "discount"
        pool = BlockingConnectionPool(decode_responses=True,
                                      timeout=5,
                                      socket_timeout=5,
                                      **kwargs).from_url(url)
        self.__conn = Redis(connection_pool=pool)

    def insert(self, url):
        data = self.__conn.sadd(self.name, url)
        return True if data else False

    def delete(self, url):
        return self.__conn.srem(self.name, url)

    def clear(self):
        return self.__conn.delete(self.name)

    def exists(self, url):
        return self.__conn.sismember(self.name, url)

    @property
    def count(self):
        return self.__conn.scard(self.name)


db = RedisClient(REDIS_CONN)

if __name__ == '__main__':
    print(db.insert("11111111"))
    print(db.exists("11111111"))
    # rd.clear()
