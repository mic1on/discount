# -*- coding: utf-8 -*-

import os
import logging
import platform

from logging.handlers import TimedRotatingFileHandler

# 日志级别
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

CURRENT_PATH = os.path.dirname(os.path.abspath(__file__))
ROOT_PATH = os.path.join(CURRENT_PATH, os.pardir)
LOG_PATH = os.path.join(ROOT_PATH, 'log')

if not os.path.exists(LOG_PATH):
    try:
        os.mkdir(LOG_PATH)
    except FileExistsError:
        pass


class LogHandler(logging.Logger):
    """
    LogHandler
    """
    def __init__(self, name, level=DEBUG, stream=True, file=False):
        self.name = name
        self.level = level
        logging.Logger.__init__(self, self.name, level=level)
        if stream:
            self.__addStreamHandler__()
        if file and platform.system() != "Windows":
            self.__addFileHandler__()

    def __addFileHandler__(self, level=None):
        file_name = os.path.join(LOG_PATH, '{name}.log'.format(name=self.name))
        # 设置日志回滚, 保存在log目录, 一天保存一个文件, 保留15天
        file_handler = TimedRotatingFileHandler(filename=file_name, when='D', interval=1, backupCount=15)
        file_handler.suffix = '%Y%m%d.log'
        file_handler.setLevel(level or self.level)
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        )
        file_handler.setFormatter(formatter)
        self.file_handler = file_handler
        self.addHandler(file_handler)

    def __addStreamHandler__(self, level=None):
        stream_handler = logging.StreamHandler()
        formatter = logging.Formatter(
            '%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s'
        )
        stream_handler.setFormatter(formatter)
        stream_handler.setLevel(level or self.level)
        self.addHandler(stream_handler)


logger = LogHandler(__name__)