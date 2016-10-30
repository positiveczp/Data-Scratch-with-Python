#-*-coding:utf-8-*-
'''
@discription：代码用来爬取各地区历练的各批次的高考分数线，然后将这些信息写入到Excel表格中
@author: CZP
'''
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import xlsxwriter
from selenium import webdriver
from bs4 import BeautifulSoup

#面向对象编程（OOP）
class Scores(object):

    def __init__(self):
        self.i = -1
        self.workbook = xlsxwriter.Workbook('scores.xlsx')
        self.worksheet = self.workbook.add_worksheet()
        self.worksheet.set_column('A:A', 10)
        self.worksheet.set_column('B:B', 10)
        self.worksheet.set_column('C:C', 10)
        self.worksheet.set_column('D:D', 10)
        self.worksheet.set_column('E:E', 10)
    #获取地区 年份 考生类别 批次 分数线
    def get_grade(self,url):
        try:
            print url
            driver = webdriver.PhantomJS()
            driver.get(url)
            data = driver.page_source

            soup = BeautifulSoup(data,'lxml')
            grades = soup.find_all('tr')
            for grade in grades:
                #判断是否是有用信息
                if '<td>'in str(grade):
                    self.i+=1
                    grade_text = str(grade.get_text())
                    #注意城市名的不统一，比如广东和内蒙古
                    city = grade_text[:-25]
                    self.worksheet.write(self.i,0,city)
                    year = grade_text[-25:-21]
                    self.worksheet.write(self.i,1,year)
                    subs = grade_text[-21:-15]
                    self.worksheet.write(self.i,2,subs)
                    s = grade_text[-15:-3]
                    self.worksheet.write(self.i,3,s)
                    scores = grade_text[-3:]
                    self.worksheet.write(self.i,4,scores)
        except:
            print 'Error!'
    def start(self):
        #待爬取的url集合
        urls = ['http://gkcx.eol.cn/soudaxue/queryProvince.html?page='+str(num) for num in range(1,22)]
        for url in urls:
            self.get_grade(url)
        self.workbook.close()

scores = Scores()
scores.start()

























