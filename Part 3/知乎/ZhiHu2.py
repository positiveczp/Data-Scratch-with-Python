#-*-coding:utf-8-*-
'''
@discription：先登录，利用cookies模拟登录知乎
@author: CZP
'''

import requests
url = 'https://www.zhihu.com/question/21361660'
cookies = {'cookies':'q_c1=4c42f7dd8b8b480dbe04ee57288c7c65|1469780606000|1467118646000; cap_id="YmRiZTJhYWJjNTVhNDY1ZjhiOTFjZmE3OGQ4ODFkZmE=|1471185362|38fe24b84ebdb8cde953b70821f22211310cd1fe"; l_cap_id="YWI1ZmJlZjBhNWJjNDM3NmI1ZDdkOGZiNWY4ZmJlOTg=|1471185362|c77ec3d46e691a7ef53302e87ac2d4792e631eb7"; d_c0="AJCAhyfZJQqPTo1Gsdzh1R3A_BsyI8RrY0w=|1467118645"; _za=28789a22-25ea-473b-ae23-21d01bed7e08; __utma=51854390.1986289492.1471162360.1471162360.1471184051.2; __utmz=51854390.1471161876.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); _zap=c23f3e19-3a24-45f1-b35f-ef14c7bd630a; login="MTQwNTg0ZjI5ZTdjNGJlZGEzNzczNThiODJiZmI0ZTc=|1471161911|2ae6eca4b631a993521a2cf598f32d6c1aa143ec"; _xsrf=2eeaa14f19a5e9d048f172f188132ade; __utmv=51854390.000--|2=registration_date=20151030=1^3=entry_date=20160628=1; __utmb=51854390.16.9.1471185328854; __utmc=51854390; s-q=python%E7%88%AC%E8%99%AB; s-i=3; sid=mer3nkhc; __utmt=1; n_c=1'}
#知乎一定要加headers,因为会检查是不是浏览器访问，而微博手机版不需要用
headers = {
            'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8',
            'Host':'www.zhihu.com',
            'Connection':'keep-alive',
            'Referer':'https://www.zhihu.com/',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
            }

response = requests.get(url,headers=headers,cookies=cookies)
print response.content













