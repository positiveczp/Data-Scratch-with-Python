#-*-coding:utf-8-*-
'''
@discription：代码用来爬取豆瓣Top250页面的图书，包括书名，评分，评分人数，封面，图书链接以及出版信息
              然后将这些信息写入到Excel表格中
@author: CZP
'''
#==========ascii编码问题==============
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import os
import re
import xlsxwriter
from bs4 import BeautifulSoup
#from datetime import datetime
import datetime
import requests

class Douban(object):

    def __init__(self):

        #创建czp文件夹,用于存放图片
        if not os.path.exists('czp'):
            os.makedirs('czp')

        self.urls = ['https://book.douban.com/top250?start='+str(num)for num in range(0,250,25)]
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'}
        #列表的索引，范围（0-24）
        self.i = -1
        #250本图书的索引，范围（0-249）
        self.index = -1
        self.workbook = xlsxwriter.Workbook('doubanbook.xlsx')
        self.worksheet = self.workbook.add_worksheet()
        #居中对齐
        format = self.workbook.add_format()
        format.set_align('justify')
        format.set_align('center')
        format.set_align('vjustify')
        format.set_align('vcenter')
        format.set_text_wrap()
        # 设置宽度和高度
        for i in range(0, 251):
            self.worksheet.set_row(i, 71)
        self.worksheet.set_column('A:A', 5,format)
        self.worksheet.set_column('B:B', 25,format)
        self.worksheet.set_column('C:C', 4,format)
        self.worksheet.set_column('D:D', 7,format)
        self.worksheet.set_column('E:E', 9,format)
        self.worksheet.set_column('F:F', 40,format)
        self.worksheet.set_column('G:G', 80,format)

    #函数过滤器
    def has_href_and_title(self,tag):
        return tag.has_attr('href')and tag.has_attr('title')

    #获取页面的信息
    def getPageInfo(self,url):
        html = requests.get(url,headers=self.headers).content
        soup = BeautifulSoup(html,'lxml')
        #获取书名
        self.booknames = soup.find_all(self.has_href_and_title)
        #获取评分
        self.ratings = soup.find_all('span',class_='rating_nums')
        #获取评分人数
        self.nums = soup.find_all('span',class_='pl')
        #删除最后一个元素
        self.nums.pop()
        #获取图书链接
        self.booklinks = soup.find_all('div',class_='pl2')
        #获取封面链接
        self.ImageUrls = soup.find_all('img',src=re.compile(r'.jpg'))
        #获取出版信息
        self.publications = soup.find_all('p',class_='pl')

    #写入索引
    def write_index(self):
        self.worksheet.write(self.index, 0, self.index)

    #写入书名
    def write_bookname(self):
        bookname = self.booknames[self.i]
        info = bookname['title'].strip()
        self.worksheet.write(self.index, 1, info)

    #写入评分
    def write_rating(self):
        rating = self.ratings[self.i]
        info = rating.text.strip()
        self.worksheet.write(self.index, 2, info)

    #写入评分人数
    def write_num(self):
        num = self.nums[self.i]
        #print num.string.replace('(','').replace(')','').replace('/n','').strip()
        #从.....人评论中提取出评论数
        pattern = re.compile(r'\d+')
        #匹配后输出的是包含字符串的列表
        info = pattern.findall(str(num))[0]
        self.worksheet.write(self.index, 3, info)

    #写入封面
    def write_image(self):
        imageurl = self.ImageUrls[self.i]
        link = imageurl.get('src')
        image = requests.get(link).content
        #命名:文件夹+'/'+文件名，将图片保存到czp文件夹中
        with open('czp'+'/'+'images'+str(self.index)+'.jpg','wb') as file:
            file.write(image)
        #从指定的文件夹czp中读取图片
        self.worksheet.insert_image(self.index, 4,'czp'+'/'+'images'+str(self.index)+'.jpg')

    #写入图书链接
    def write_links(self):
        link = self.booklinks[self.i]
        info = link.a.get('href')
        self.worksheet.write(self.index, 5, info)

    #写入出版信息
    def write_publication(self):
        pub = self.publications[self.i]
        info = pub.string
        self.worksheet.write(self.index, 6, info)

    #开始
    def start(self):
        #starttime = datetime.now()
        starttime = datetime.datetime.now()
        print '采集计时开始：%s'%starttime
        for url in self.urls:
            print url
            self.getPageInfo(url)

            for self.i in range(0,25):
                self.index += 1
                self.write_index()
                self.write_bookname()
                self.write_rating()
                self.write_num()
                self.write_image()
                self.write_links()
                self.write_publication()
        self.workbook.close()

        #endtime = datetime.now()
        endtime = datetime.datetime.now()
        print '采集结束:%s'%endtime
        print '用时%s'%(endtime-starttime)
douban = Douban()
douban.start()




































































