# -*-coding:utf-8-*-
'''
@discription：通过输入百度贴吧帖子的编号来抓取贴吧上的内容，并对爬取到的内容进行格式化处理
@author: CZP
'''
import urllib2
import re


# 页面处理类
class Tool:
    # 去除img标签
    removeImg = re.compile('<img.*?>| {7}')
    # 去除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行符或双换行符替换为 \n
    replaceBR = re.compile('<br><br>|<br>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceBR, "\n", x)

        return x


# 百度贴吧爬虫类
class BDTB:
    # 初始化，传人基地址以及是否只看楼主的参数
    def __init__(self, baseUrl, seeLZ, floorTag):
        # base链接地址
        self.baseUrl = baseUrl
        # 是否只看楼主
        self.seeLZ = '?see_lz=' + str(seeLZ)
        self.tool = Tool()
        # 全局file变量，文件写入操作对象
        self.file = None
        # 楼层初始化标志
        self.floor = 1
        # 是否写入楼分隔的标记
        self.floorTag = floorTag
        # 默认的标题，如果没有成功获取到标题的话则会用到这个标题
        self.defaultTitle = "百度贴吧"

    # 传入页码，获取帖子的html代码
    def getPage(self, pageNum):
        try:
            url = self.baseUrl + self.seeLZ + "&pn=" + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf8', 'ignore').encode('mbcs')

        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print "连接百度贴吧失败，失败原因", e.reason
                return None

    # 获取帖子的标题
    def getTitle(self, page):
        # 获取标题的正则表达式
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern, page)
        # 输出结果
        if result:
            return result.group(1).strip()
        else:
            print 'failed'

            # 获取帖子一共多少页

    def getPageNum(self, page):
        # 获取正则表达式
        pattern = re.compile('<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern, page)
        # 输出结果
        if result:
            return result.group(1)
        else:
            print 'failed'

            # 提取每一楼的内容

    def getContent(self, page):
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern, page)
        contents = []
        for item in items:
            content = "\n" + self.tool.replace(item) + "\n"
            contents.append(content)
        return contents

    def setFileTitle(self, title):
        # 如果标题不是None，则成功获取到标题
        if title is not None:
            self.file = open(title + ".txt", "w+")
        else:
            self.file = open(self.defaultTitle + ".txt", "w+")

    def writeDate(self, contents):
        # 向文件写入每一楼的信息
        for item in contents:
            if self.floorTag == '1':
                # 楼之间的分隔符
                floorline = "\n" + str(
                    self.floor) + "=========================================================================================================================\n"
                self.file.write(floorline)
            self.file.write(item)
            self.floor += 1

    def start(self):
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum == None:
            print "URL已失效，，请重试"
            return
        try:
            print"该帖子共有" + str(pageNum) + "页"
            for i in range(1, int(pageNum) + 1):
                print "正在写入第" + str(i) + "页数据"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeDate(contents)
        # 出现写入异常
        except IOError, e:
            print "写入异常，原因" + e.reason

        finally:
            print "写入任务结束"


print "请输入帖子代号"
baseURL = 'http://tieba.baidu.com/p/' + str(raw_input('http://tieba.baidu.com/p/'))
seeLZ = raw_input("是否指获取楼主发言，是输入1，否输入0\n")
floorTag = raw_input("是否写入楼层消息，是输入1，否输入0\n")
# BDTB的对象
bdtb = BDTB(baseURL, seeLZ, floorTag)
# 开始
bdtb.start()













































