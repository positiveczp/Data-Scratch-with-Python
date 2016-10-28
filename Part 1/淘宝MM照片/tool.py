# -*-coding:utf-8-*-
import re


# 页面处理类
class Tool:
    # 去除img标签
    removeImg = re.compile('<img.*?>| {7}')
    # 去除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行符或双换行符替换为 \n
    replaceBR = re.compile('<br><br>|<br>')

    def replace(self, x):
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        x = re.sub(self.replaceBR, "\n", x)

        return x
















