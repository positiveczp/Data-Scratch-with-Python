# -*-coding:utf-8-*-
'''
@discription：代码用来爬取糗事百科上的笑话
@author: CZP
'''
import re
import urllib2

url = 'http://www.qiushibaike.com/8hr/page/3/?s=4901238'
headers = {'User-Agent': 'Mozilla/4.0'}

try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    content = response.read()
    pattern = re.compile('<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<a href.*?>(.*?)</a>.*?<i class="number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        haveImg = re.search("img", item[2])

        if not haveImg:
            replace = re.compile('<br/>')
            text = re.sub(replace, "/n", item[1])
            print item[0].strip() + '\t' + item[3].strip()
            print text.strip()
            print

except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason





