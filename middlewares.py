# -*- coding: utf-8 -*-

from fake_useragent import UserAgent
import base64


# 随机更换user-agent
class RandomUserAgentMiddleware(object):

    def __init__(self, crawler):
        super().__init__()
        self.ua = UserAgent()

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def process_request(self, request, spider):
        request.headers.setdefault("User-Agent", self.ua.random)


# 设置代理 创建一个中间件，在每个Request发出去之前，补充上代理IP的信息
class ProxyMiddleware(object):
    # overwrite process request
    def process_request(self, request, spider):
        # 设置代理的主机和端口号
        request.meta['proxy'] = "Your proxy ip"

        # 设置代理的认证用户名和密码
        proxy_user_pass = "user:password"
        encoded_user_pass = base64.encodestring(proxy_user_pass)

        # 设置代理
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
