#-*-coding:utf-8-*-
#==========================selenium处理动态加载和多进程爬取==========================================
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from datetime import datetime
from multiprocessing import Pool

global i,songnumber,Base_URL,Page_URL,driver
i = 0
songnumber = 0
Base_URL = 'http://music.163.com'
Page_URL = 'http://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset='
driver = webdriver.PhantomJS()
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Host': 'music.163.com',
    'Referer': 'https://www.music.163.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

#获取歌单的所有href
def getSongshref(PageNum):

    #try:
    songs_href = []
    Full_URL = Page_URL + str(PageNum)
    html = requests.get(url=Full_URL,headers=headers).content
    soup = BeautifulSoup(html,'lxml')
    songlists = soup.find_all('a',class_="msk")
    for song in songlists:
         songs_href.append(song["href"])
    # 35个href
    return songs_href
    #except:
        #print "Error!"

#获取所有单曲的详细信息
def getSongInfo(PageNum,href):

    #try:
    full_URL = Base_URL + href
    driver.get(full_URL)
    #定位到iframe，非常关键
    driver.switch_to_frame('g_iframe')
    time.sleep(2)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    #评论数
    number = soup.find('span', class_='j-flag').string
    #歌曲
    song = soup.find('em', class_='f-ff2').string
    #歌手
    singer = soup.find('p', class_='des s-fc4').find('span')['title']
    songnumber += 1
    if int(number) > 10000:
        i += 1
        print i,":",number,"====>",song + "//" + singer,"====>",full_URL,"(" + str(PageNum/35) + ")"
    #except:
        #print "Error!"


#获取所有单曲的href
def getSonghref(PageNum):

    #try:
    songs_href = getSongshref(PageNum)
    #35个href
    for href in songs_href:
        full_URL = Base_URL + href
        driver.get(full_URL)
        #定位到iframe，非常关键
        driver.switch_to_frame('g_iframe')
        time.sleep(2)
        html = driver.page_source
        soup = BeautifulSoup(html, 'lxml')
        AllSongs = soup.find_all('span',class_='txt')
        for song in AllSongs:
            song_href = song.find('a')['href']
            getSongInfo(PageNum,song_href)
    #except:
        #print "Error!"




if __name__ == '__main__':

    starttime = datetime.now()
    p = Pool()
    for i in range(0,2):
        p.map_async(getSonghref,(35*i,))
    p.close()
    p.join()





































































