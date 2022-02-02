# -*- coding: utf-8 -*-

# 消息通知启用渠道配置
CHANNELS = {
    'PUSHDEER': {
        'TOKEN': 'PDU3862TwwU3VVIYMfND6xSbj0PXVKJSqorE4Htv'
    }
}
# 消息通知启用触发器
TRIGGERS = {
    'notify.channels.pushdeer.PushDeer': 100,
}

REDIS_CONN = 'redis://localhost:6379/1'


SPIDERS = [
    "guang_diu",
    "smzdm"
]

SEARCH_WORDS = [
    "可心柔 保湿抽纸",
    "全棉时代 湿纸巾",
    "光羽 s码"
]

# 线程数量
MAX_WORKERS = 5