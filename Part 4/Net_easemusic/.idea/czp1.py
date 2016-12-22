#-*-coding:utf-8-*-
import requests
from bs4 import BeautifulSoup
import re,time

headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'https://www.music.163.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
          }
html = requests.get(url=Page_URL,headers=headers).content

soup = BeautifulSoup(html,'lxml')
songlists = soup.find_all('a',class_="msk")
for song in songlists:
    List_URL = Base_URL + song["href"]
    html = requests.get(url=List_URL).content
    soup = BeautifulSoup(html, 'lxml')
    print html
    #========================网易云音乐的评论数和页面内容是动态JS加载的============
    #AllSongs = soup.find_all('span',class_='txt')
    #for song in AllSongs:
       #print song.find('a')['href']









































