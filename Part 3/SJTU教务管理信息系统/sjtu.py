# -*-coding:utf-8-*-
'''
@discription：利用提交表单的方式模拟登陆SJTU教务管理信息系统
@author: CZP
'''

import requests
import re
import webbrowser


class SJTU:
    def __init__(self):
        self.loginUrl = 'https://jaccount.sjtu.edu.cn/jaccount/jalogin?sid=jagraduate20130107&returl=CEJxTC9big90u3wTIqHUYtHzDupI5IkvGHoDj3yNrNNyE529QBZ5qL3l2aqTPVxmR73ypuy3g7sFOsPmT57TCC2c5OcKSGs3zg139x2%2bk%2bw3b9vXFQ%2buHgGHXwkWuJ5CeQ%3d%3d&se=CGvDFHXgijPvu48Zj7WF4QooSVDOiC9qvEkOs91n1%2bUl'
        self.postUrl = 'https://jaccount.sjtu.edu.cn/jaccount/ulogin'
        self.se = self.getSe(self.getHtml())
        self.returl = self.getReturl(self.getHtml())
        self.captcha = self.getCaptcha(self.getHtml())
        self.data = {

            'sid': 'jagraduate20130107',
            'returl': self.returl,
            'se': self.se,
            'v': '',
            'user': 'positive****',
            'pass': 'czp885****',
            'captcha': self.captcha
        }
        self.headers = {
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie':'JSESSIONID=B1C0742B83F500EA280C85922FC04537.jaccount106; JAVisitedSites="CAVYPqNdvbr2p5auOw91L70OWmjVUZOCPtAvADmbjmm/GioCyheJqxnvPN+4KiHKoQ=="; JACCOUNT=jaccount.older107',
            'Host':'jaccount.sjtu.edu.cn',
            'Origin':'https://jaccount.sjtu.edu.cn',
            'Referer':'https://jaccount.sjtu.edu.cn/jaccount/jalogin?sid=jagraduate20130107'+'&returl='+str(self.returl)+'&se='+str(self.se),
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }

    def begin(self):
        login_result = requests.post(self.postUrl, data=self.data, headers=self.headers)
        result = requests.get(url=self.loginUrl)
        print result.content.decode('utf8', 'ignore').encode('mbcs')

    def getHtml(self):
        result = requests.get(self.loginUrl)
        return result.content.decode('utf8', 'ignore').encode('mbcs')

    def getReturl(self, page):
        pattern = re.compile(r'<.*?name="returl" value="(.*?)">', re.S)
        content = re.search(pattern, page)

        print content.group(1)
        return content.group(1)

    def getSe(self, page):
        pattern = re.compile(r'<.*?name="se" value="(.*?)"', re.S)
        content = re.search(pattern, page)

        print content.group(1)
        return content.group(1)

    def getCaptcha(self, page):
        pattern = re.compile(r'<div.*?name="captcha".*?<img src="(.*?)"', re.S)
        content = re.search(pattern, page)
        code = 'https://jaccount.sjtu.edu.cn/jaccount/' + str(content.group(1))
        webbrowser.open_new_tab(code)
        checkcode = raw_input('请输入验证码：')
        return checkcode


sjtu = SJTU()
sjtu.begin()




































