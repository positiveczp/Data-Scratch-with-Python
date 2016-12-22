#-*-coding:utf-8-*-
import requests
from selenium import webdriver
import time
from bs4 import BeautifulSoup

url = "http://music.163.com/#/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=0"
driver = webdriver.PhantomJS()
driver.get(url)
driver.switch_to_frame('g_iframe')
time.sleep(2)
html = driver.page_source
soup = BeautifulSoup(html, 'lxml')
songs = soup.find_all('p', class_='dec')
for song in songs:
    print song.find('a')['title']










