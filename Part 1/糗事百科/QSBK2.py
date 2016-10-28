# -*-coding:utf-8-*-
'''
@discription：代码用来显示爬取到的糗事百科上的每个笑话
@author: CZP
'''
import re
import urllib2


class QSBK:
    # 初始化方法，定义一些变量
    def __init__(self):
        self.user_agent = 'Mozilla/4.0'
        # 初始化headers
        self.headers = {'User-Agent': self.user_agent}
        self.enable = False
        # 存放段子的变量
        self.pagestories = []

    def getPage(self):
        try:
            url = 'http://www.qiushibaike.com/8hr/page/3/?s=4901238'
            request = urllib2.Request(url, headers=self.headers)
            response = urllib2.urlopen(request)
            pagehtml = response.read()
            return pagehtml
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print "连接糗事百科失败，错误原因", e.reason
                return None

    def getPageItems(self):
        pagehtml = self.getPage()
        if not pagehtml:
            print '加载失败........'
            return None
        pattern = re.compile('<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<a href.*?>(.*?)</a>.*?<i class="number">(.*?)</i>',re.S)
        items = re.findall(pattern, pagehtml)

        for item in items:
            haveImg = re.search("img", item[2])
            # 如图不含图片，加进list中
            if not haveImg:
                replace = re.compile('<br/>')
                text = re.sub(replace, "\n", item[1])
                self.pagestories.append([item[0].strip(), text.strip(), item[3].strip()])

        return self.pagestories

    def getOneStory(self, pagestorise):
        for story in self.pagestories:
            # 等待用户输入
            a = raw_input('输入回车显示：')
            if a == "q":
                self.enable = False
                return
            print "发布人：%s\t赞:%s\n%s" % (story[0], story[2], story[1])

    # 开始方法
    def start(self):
        print "正在读取糗事百科，按回车查看段子，q退出"
        self.enable = True
        # 只有为True，一直进行下去
        while self.enable:
            self.getOneStory(self.getPageItems())


if __name__ == "__main__":
    spider = QSBK()
    spider.start()












































































