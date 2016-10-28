# -*-coding:utf-8-*-
# ===========================成功爬取到MM照片======================================

__author__ = 'CZP'
import urllib2
import re
import os


class Spider:
    def __init__(self):
        self.siteURL = 'https://mm.taobao.com/tyy6160'

    def getPage(self):
        request = urllib2.Request(self.siteURL)
        response = urllib2.urlopen(request)
        return response.read().decode('gbk')

    def getAllImg(self, page):
        pattern = re.compile('<img.*?src="(.*?)"', re.S)
        images = re.findall(pattern, page)
        return images

    def saveImgs(self, images, name):
        number = 1
        print "发现", name, "共有", len(images), "张照片"
        for imageURL in images:
            splitPath = imageURL.split('.')
            fTail = splitPath.pop()
            if fTail != 'jpg':
                fTail = 'jpg'
            filename = name + "/" + str(number) + "." + fTail
            self.saveImg(('http:' + imageURL.strip()), filename)
            number += 1

    def saveImg(self, imageURL, fileName):
        # 异常处理
        try:
            u = urllib2.urlopen(imageURL)
            data = u.read()
            f = open(fileName, 'wb')
            f.write(data)
            print "正在悄悄保存她的一张照片为", fileName
            f.close()
        except:
            print 'craw failed'

    def mkdir(self, path):
        path = path.strip()
        isExists = os.path.exists(path)

        if not isExists:
            print "偷偷新建名字叫做", path, "的文件夹"
            os.makedirs(path)
        else:
            print '名为', path, '的文件夹已经创建成功'

    def savePageInfo(self):
        images = self.getAllImg(self.getPage())
        self.mkdir('XXX')
        self.saveImgs(images, 'XXX')


spider = Spider()
spider.savePageInfo()

































































