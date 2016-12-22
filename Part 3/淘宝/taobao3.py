#-*-coding:utf-8-*-
#======================利用selenium爬取淘宝==============================
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
import time
import os

class TaoBao(object):

    def __init__(self):
        url = 'https://world.tmall.com/item/45262540681.htm?spm=a220m.1000858.1000725.110.r7oyq2&id=45262540681&skuId=85225485607&areaId=320700&cat_id=50025145&rn=6f644caecfa85abefea71e2dc48ac6ae&user_id=2148264599&is_b=1'
        self.driver = webdriver.Chrome()
        self.driver.get(url)

    def getPage(self):
        try:

            #模拟浏览器向下滑动
            self.driver.maximize_window()
            time.sleep(10)
            self.driver.execute_script("window.scrollBy(0,2000)")
            #页面加载时间
            time.sleep(10)
            self.driver.execute_script("window.scrollBy(2000,4000)")
            time.sleep(10)
            self.driver.execute_script("window.scrollBy(4000,8000)")
            time.sleep(10)
            WebDriverWait(self.driver,30).until(EC.presence_of_element_located((By.CLASS_NAME,"ald-wf-li")))
            return self.driver.page_source
        except TimeoutException:
            print "TimeoutException!"

    def getPageLinks(self):
        html = self.getPage()
        soup = BeautifulSoup(html,'lxml')
        return soup.find_all('a',class_='ald-wf-pic')

    def start(self):
        #创建文件夹
        if not os.path.exists('LINKS'):
            os.makedirs('LINKS')

        links = self.getPageLinks()
        print '开始写入链接！'
        number = 0
        # 命名:文件夹+'/'+文件名，将链接保存到LINKS文件夹中
        file = open('LINKS'+'/'+'links.txt','w')
        for link in links:
            number += 1
            file.write("第%d个链接: " %number)
            file.write('https:'+link.get('href'))
            file.write('\n')
        print '所有链接写入完毕！总共写入%d个链接！' %number
        file.close()

taobao = TaoBao()
taobao.start()












































