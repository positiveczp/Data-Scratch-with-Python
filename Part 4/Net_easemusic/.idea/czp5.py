#-*-coding:utf-8-*-
import requests
import datetime
import multiprocessing
from bs4 import BeautifulSoup
import time

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'music.163.com',
    'Referer': 'https://www.music.163.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

def getSongshref(PageNum):
    Page_URL = 'http://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset=' + str(PageNum)
    songs_href = []
    html = requests.get(url=Page_URL,headers=headers).content
    soup = BeautifulSoup(html, 'lxml')
    songlists = soup.find_all('a', class_="msk")
    for song in songlists:
         songs_href.append(song["href"])
    # 35个href
    return songs_href


if __name__ == '__main__':

    start = datetime.datetime.now()
    # 多进程抓取
    p = multiprocessing.Pool()
    for i in range(0,2):
        p.apply_async(getSongshref,args=(35*i,))
    p.close()
    p.join()


























