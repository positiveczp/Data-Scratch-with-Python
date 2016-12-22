# [Python](https://www.python.org/) 爬虫学习路线
* Python版本--2.7.11版本
* IDE开发环境--PyCharm
* 运行平台--Windows 7
* Python入门书籍推荐--[《Python简明教程》](http://www.kuqin.com/abyteofpython_cn/)

## Part1、Python爬虫初窥
### ——第一部分主要学习python爬虫过程中用到的一些基本的工具

#### 网页页面下载的工具
* [Urllib2](http://www.pythontab.com/html/2014/pythonhexinbiancheng_1128/928.html)
* [Requests](http://cn.python-requests.org/zh_CN/latest/)

#### 页面内容提取的工具
* [正则表达式](http://www.runoob.com/regexp/regexp-syntax.html)
* [BeautifulSoup](http://beautifulsoup.readthedocs.io/zh_CN/latest/)
* [lxml](http://lxml.de/index.html) & [Xpath](http://www.cnblogs.com/Loofah/archive/2012/05/10/2494036.html)

#### 实战项目
* [百度百科词条](http://baike.baidu.com/link?url=VKUmqgxu-6b4jGRoISesZ9YoB0JPlr1w76zO7CxAyXD-5QCXVnHCVSN0nMNeT95djAp-rSgud64fdZ3S4qSBZa)
* [糗事百科](http://www.qiushibaike.com/)
* [百度贴吧](http://tieba.baidu.com/)
* [淘宝MM照片](https://mm.taobao.com/json/request_top_list.htm?page=1)

## Part2、数据的简单存储
### ——第二部分学习将数据存放到Excel、MySQL & MongoDB中
#### 通过第一部分的学习我们已经学会如何将爬取到的数据存储在txt文件中了，这一部分主要简单介绍如何利用[pymongo](http://api.mongodb.com/python/current/)、[MySQLdb](http://mysql-python.sourceforge.net/MySQLdb.html)、[xlsxwriter](https://xlsxwriter.readthedocs.io/)这些模块将数据存放到Excel表格、MySQL&MongoDB数据库中
* [Excel](http://xlsxwriter.readthedocs.io/)
* [MySQL](http://www.runoob.com/python/python-mysql.html)
* [MongoDB](http://www.jianshu.com/p/5c4cd03d29ae)

#### 实战项目
* [高考分数线](http://gkcx.eol.cn/soudaxue/queryProvince.html?page)
* [豆瓣图书Top250](https://book.douban.com/top250?start=0)

## Part3、登录页面的爬取
### ——第三部分介绍如何爬取需要登录的页面
#### 有很多页面都是需要我们登录了才能够访问的，比如[知乎](https://www.zhihu.com/)，[新浪微博](http://weibo.com/?c=spr_web_sq_firefox_weibo_t001&sudaref=e.firefoxchina.cn&retcode=6102)，[豆瓣](https://www.douban.com/)，[淘宝](https://www.taobao.com/)我们在这一部分介绍两种爬取需要登录页面的方法；分别是表单提交和利用[Selenium](http://docs.seleniumhq.org/)来控制浏览器

#### 实战项目
* [知乎](https://www.zhihu.com/)
* [手机&电脑版新浪微博](http://weibo.com/?c=spr_web_sq_firefox_weibo_t001&sudaref=e.firefoxchina.cn&retcode=6102)
* [豆瓣](https://www.douban.com/)
* [qq空间](http://qzone.qq.com/)
* [SJTU教务管理信息系统](https://jaccount.sjtu.edu.cn/jaccount/jalogin?sid=jafinance20150602&returl=%43%46%75%44%51%77%4a%49%4e%5a%73%74%70%58%67%44%6a%71%43%43%49%38%57%53%71%59%42%43%76%58%58%53%52%67%56%43%46%31%53%31%44%6b%5a%59%39%41%65%6e%64%66%37%36%54%65%41%76%78%31%6f%68%4b%6f%79%2f%50%51%33%65%36%38%45%49%4f%46%47%45&se=%43%48%31%52%65%63%6c%48%6b%69%4a%72%2b%36%45%73%2f%68%78%49%46%56%76%35%79%57%4b%6f%76%6d%75%34%53%54%72%55%47%63%4a%32%31%55%78%39%43%49%2f%50%71%59%58%69%67%58%2b%4b%6a%45%41%44%64%64%47%4f%72%51%3d%3d&v=20120509)
* [GDUT教务管理信息系统](http://jwgldx.gdut.edu.cn/)


## Part4、初识[多进程](http://blog.csdn.net/u011497904/article/details/44288771)、[多线程](http://www.jianshu.com/p/86b8e78c418a?search_token=4d8e9a843325f3abd4be64fb668ec7812f760bc1f9aa7b10431fa8966453a868)&[协程](http://www.jb51.net/article/88825.htm)
### ——第四部分主要简单的介绍多线程、多线程和协程的基本概念
#### 为了提高我们的爬虫爬取的速度，于是在原有的单进程的基础上，我们引入了多进程和多线程的概念，它可以大幅度提高我们爬取的效率

#### 实战项目
* [网易云音乐](http://music.163.com/)

## Part5、[Scrapy](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)框架
### ——第五部分介绍一个非常强大的爬虫框架[Scrapy](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)
#### Scrapy是一个使用Python编写的，轻量级的框架，可以大大提高开发的效率，缩短开发的时间
#### 实战项目
* [豆瓣图书Top250](https://book.douban.com/top250?start=0)
* [satomi_pic](http://movie.douban.com/celebrity/1016930/photo/1253599819/#photo)
* [airi_pic](http://tieba.baidu.com/p/4023230951)




