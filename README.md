本报程序目的是自动找出全网优惠商品，及时推送给自己
#### 新增消息通知接收方
:grin:[简易消息通知](https://github.com/mic1on/simple-notify)
#### 扩充渠道源

当内置渠道无法满足优惠线报需求，可自定义增加渠道，方法如下：
在spiders/spiders.py的Spiders类中：
```python
@staticmethod
def my_custom(word):
    url = f'your_custom_url'
    parser = Request().get(url).encode.parser
    a_lst = parser.xpath("a标签定位")
    for a in a_lst:
        yield dict(title=a.xpath('./@title').get(),
                   href=a.xpath('./@href').get())
```
在settings.py中启用它：
```python
SPIDERS = [
    ...
    "my_custom"
]
```
> 注意：必须是静态方法

#### 新增搜索商品关键词
在settings.py中新增关键词：
```python
SEARCH_WORDS = [
    ...
    "自定义搜索内容"
]
```