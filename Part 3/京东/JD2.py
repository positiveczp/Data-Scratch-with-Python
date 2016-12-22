#-*-coding:utf-8-*-
#======================利用selenium爬取京东页面商品信息==============================
import time
from selenium import webdriver
from lxml import etree

driver = webdriver.PhantomJS()
driver.get('http://item.jd.com/2664405.html')
time.sleep(2)
html = driver.page_source
selector = etree.HTML(html)
name = selector.xpath('//div[@class="sku-name"]')#获取文本内容可以通过/text()或.text
price = selector.xpath('//span[@class="price J-p-2664405"]/text()')#获取文本内容可以通过/text()或.text
print price[0]
print name[0].text
driver.close()





























