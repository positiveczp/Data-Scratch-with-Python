# -*-coding:utf-8-*-
'''
@discription：利用提交表单的方式模拟登陆知乎
@author: CZP
'''
import urllib2
import urllib
import re
import cookielib
import webbrowser
import time


class ZhiHu(object):
    def __init__(self):
        self.url = 'https://www.zhihu.com/#signin'
        self.loginUrl = 'http://www.zhihu.com/login/phone_num'
        self.cookies = cookielib.CookieJar()
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        self.xsrf = self.getxsrf()
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0',
                        'Host': 'www.zhihu.com',
                        'Referer': 'http://www.zhihu.com/'
                        }
        self.data = {"password": "czp885****", "remember_me": "true", "phone_num": "1582189****", '_xsrf': self.xsrf}
        self.postdata = urllib.urlencode(self.data)
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0'}

    def getxsrf(self):
        request = urllib2.Request(self.url)
        page = self.opener.open(request).read()
        pattern = re.compile('<input type.*?xsrf.*?value="(.*?)"', re.S)
        result = re.search(pattern, page)
        return result.group(1)

    # src="/captcha.gif?r=1470819811311&type=login"
    def getIdenCode(self):
        # t =str(int(time.time()*1000))
        captcha = 'http://www.zhihu.com/captcha.gif?r=1470914762048' + '&type=login'
        return captcha

    def Login(self):
        webbrowser.open_new_tab(self.getIdenCode())
        checkcode = raw_input('请输入验证码：')
        self.data['captcha'] = checkcode
        self.postdata = urllib.urlencode(self.data)
        request = urllib2.Request(self.loginUrl, self.postdata, self.headers)
        response = self.opener.open(request)
        print response.read().decode('utf-8').encode('mbcs')
        # newurl = 'https://www.zhihu.com/question/21395276#answer-41804535'
        # result = self.opener.open(newurl)
        # result.read().decode('utf-8')


ZhiHu = ZhiHu()
ZhiHu.Login()

































