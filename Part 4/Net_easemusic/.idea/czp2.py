#-*-coding:utf-8-*-
#==========================selenium处理动态加载==========================================
from selenium import webdriver
import time
from bs4 import BeautifulSoup
import requests
from datetime import datetime


class Net_Ease_Music(object):

    def __init__(self):

        self.i = 0
        self.songnumber = 0
        self.Base_URL = 'http://music.163.com'
        self.Page_URL = 'http://music.163.com/discover/playlist/?order=hot&cat=%E5%85%A8%E9%83%A8&limit=35&offset='
        self.driver = webdriver.PhantomJS()
        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Host': 'music.163.com',
            'Referer': 'https://www.music.163.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
        }

    #获取歌单的所有href
    def getSongshref(self,PageNum):

        try:
            songs_href = []
            Full_URL = self.Page_URL + str(PageNum)
            html = requests.get(url=Full_URL,headers=self.headers).content
            soup = BeautifulSoup(html,'lxml')
            songlists = soup.find_all('a',class_="msk")
            for song in songlists:
                 songs_href.append(song["href"])
            # 35个href
            return songs_href
        except:
            print "Error!"

    #获取所有单曲的href
    def getSonghref(self,PageNum):

        try:
            songs_href = self.getSongshref(PageNum)
            #35个href
            for href in songs_href:
                full_URL = self.Base_URL + href
                self.driver.get(full_URL)
                #定位到iframe，非常关键
                self.driver.switch_to_frame('g_iframe')
                time.sleep(2)
                html = self.driver.page_source
                soup = BeautifulSoup(html, 'lxml')
                AllSongs = soup.find_all('span',class_='txt')
                for song in AllSongs:
                    song_href = song.find('a')['href']
                    self.getSongInfo(PageNum,song_href)
        except:
            print "Error!"

    #获取所有单曲的详细信息
    def getSongInfo(self,PageNum,href):

        try:
            full_URL = self.Base_URL + href
            self.driver.get(full_URL)
            #定位到iframe，非常关键
            self.driver.switch_to_frame('g_iframe')
            time.sleep(2)
            html = self.driver.page_source
            soup = BeautifulSoup(html, 'lxml')
            #评论数
            number = soup.find('span', class_='j-flag').string
            #歌曲
            song = soup.find('em', class_='f-ff2').string
            #歌手
            singer = soup.find('p', class_='des s-fc4').find('span')['title']
            self.songnumber += 1
            if int(number) > 10000:
                self.i += 1
                print self.i,":",number,"====>",song + "//" + singer,"====>",full_URL,"(" + str(PageNum/35) + ")"
        except:
            print "Error!"

    def start(self):

        starttime = datetime.now()
        for i in range(0,42):
            self.getSonghref(i*35)
        endtime = datetime.now()
        time = endtime - starttime
        print "总共耗时%s" % time
        print self.songnumber

if __name__ == '__main__':
    music = Net_Ease_Music()
    music.start()















































