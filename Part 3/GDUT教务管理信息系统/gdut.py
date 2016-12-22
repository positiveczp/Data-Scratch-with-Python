# -*-coding:utf-8-*-
'''
@discription：利用提交表单的方式模拟登陆GDUT教务管理信息系统
@author: CZP
'''

import requests
import re
import webbrowser


class GDUT:
    def __init__(self):
        self.Url = 'http://jwgl.gdut.edu.cn/xsdjkscx.aspx?xh=3111002994&xm=陈梓平&gnmkdm=N121606'
        self.loginUrl = 'http://jwgl.gdut.edu.cn/default2.aspx'
        self.postUrl = 'http://jwgl.gdut.edu.cn/default2.aspx'
        self.checkcode = self.getCheckcode(self.getHtml())
        self.data = {
            '_VIEWSTATE': 'dDwyODE2NTM0OTg7Oz6jn4M6KToflSkkQqlKPHU+Z90VNA==',
            'txtUserName': '311100****',
            'TexBox2': 'czp885****',
            'txtSecretCode': self.checkcode
        }
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'ASP.NET_SessionId=ybcuhov20r5szinqaoxhfree',
            'Host': 'jwgl.gdut.edu.cn',
            'Origin': 'http://jwgl.gdut.edu.cn',
            'Referer': 'http://jwgl.gdut.edu.cn/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }

    def begin(self):
        login_result = requests.post(self.postUrl, data=self.data, headers=self.headers)
        result = requests.get(url=self.Url, headers=self.headers)
        print result.content

    def getHtml(self):
        result = requests.get(self.loginUrl)
        return result.content.decode('gbk', 'ignore').encode('mbcs')

    def getCheckcode(self, page):
        pattern = re.compile(r'img id="icode" src="(.*?)"', re.S)
        content = re.search(pattern, page)
        webbrowser.open_new_tab(content.group(1))
        checkcode = raw_input('请输入验证码：')
        return checkcode


gdut = GDUT()
gdut.begin()




































