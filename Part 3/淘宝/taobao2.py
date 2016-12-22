# -*-coding:utf-8-*-
#======================利用selenium爬取淘宝页面信息==============================
from bs4 import BeautifulSoup
import requests
import time
import urllib2
from selenium import webdriver
# 防止出现乱码
import sys
reload(sys)
sys.setdefaultencoding('utf8')

driver = webdriver.PhantomJS()
driver.get('https://s.taobao.com/search?q=surface&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.7724922.8452-taobao-item.1&ie=utf8&initiative_id=tbindexz_20160228')
time.sleep(7)

html = driver.page_source

soup = BeautifulSoup(html, 'lxml')
ImageUrl = soup.find_all(class_='J_ItemPic img')

k = 1
for Url in ImageUrl:
    # 加入异常处理
    try:
        print '正在写入当前帖子的第%d张图片，请等待' % k
        # 图片写入到image文件夹中，图片格式是jpg
        fp = open('image' + str(k) + '.jpg', 'wb')
        fullurl = 'http:' + Url.get('data-src')
        print fullurl
        image = urllib2.urlopen(fullurl).read()
        fp.write(image)
        print '第%d张图片写入完成' % k
        fp.close()
        k += 1
    except:
        print '出错！'

driver.get_screenshot_as_file('screenshot.jpg')
driver.close()

print '所有图片写入完成！'







