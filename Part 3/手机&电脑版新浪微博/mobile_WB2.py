#-*-coding:utf-8-*-
'''
@discription：#先登录，利用cookies模拟登陆手机版微博
@author: CZP
'''
import requests

url = 'http://weibo.cn/?tf=5_009&vt=4'
cookies = {'cookies':'_T_WM=0f948d6507a734fe70a2f969c4c098fb; SCF=AsjCdnGdKrW3r-EnN_l8gWeXLZYYSST9O6MkJ2q4M3C4bwv-Lj0fyOFxpXHTkfAf7NX7BVk3K59a-sNHBrRKtIg.; SUHB=0vJJl_zfDBvby_; SUB=_2AkMg7OdvdcNhrAFTkfAUzG7kZYxH-jzEiebBAn7oJhMyPRgv7nYyqSei-WbVKfCg7LM7F3l93ocC-ZBgzw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhWNJnG8f2_0UV-YaQuq1lM5JpX5KMhUgL.FozE1Knpeh-c1K22dJLoIXnLxK.L1K.L1hnLxKqLBKzL1KeLxK-LBo.LBoeLxKBLBo.L12zLxKML12eLBoBLxKBLBo.L12zLxKBLB.eLBK5LxKBLB.2LB.2t'}

response = requests.get(url,cookies=cookies)
print response.content.decode('utf8','ignore').encode('utf8')













