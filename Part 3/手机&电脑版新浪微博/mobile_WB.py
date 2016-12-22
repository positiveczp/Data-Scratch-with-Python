# -*-coding:utf-8-*-
'''
@discription：# 通过提交表单数据的方式模拟登录手机版微博
@author: CZP
'''
import requests
import re


class Weibo:
    def __init__(self):
        # 访问微博的网址
        self.loginUrl = 'http://weibo.cn/chiaotunguniv?vt=4'
        # 当PostUrl出现中文时，需要在action处找到相应的编码，否则会报错
        self.PostUrl = "http://login.weibo.cn/login/?rand=1397231349&amp;backURL=http%3A%2F%2Fweibo.cn%2F&amp;backTitle=%E5%BE%AE%E5%8D%9A&amp;vt=4&amp;revalid=2&amp;ns=1"
        self.data = {
            'mobile': '1882515****',
            'password_8566': 'czp885****',
            'code': 'dwmm',
            'remember': 'on',
            'backURL': 'http%3A%2F%2Fweibo.cn%2F',
            'backTitle': '微博',
            'tryCount': '',
            'vk': '8566_4ab6_2327800237',
            'capId': '2_f92a8b70242ff3cf',
            'submit': '登录'
        }
        # 这里要特别注意Host这个参数
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
            'Host': 'weibo.cn',
            'Connection': 'keep-alive',
            'Referer': 'http://login.weibo.cn/login/?ns=1&revalid=2&backURL=http%3A%2F%2Fweibo.cn%2F&backTitle=%CE%A2%B2%A9&vt=4',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }

    def begin(self):
        login_result = requests.post(self.PostUrl, data=self.data, headers=self.headers)
        result = requests.get(url=self.loginUrl, headers=self.headers)
        print result.content.decode('utf8', 'ignore').encode('mbcs')


Weibo = Weibo()
Weibo.begin()























