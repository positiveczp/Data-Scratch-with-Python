#-*-coding:utf-8-*-
import MySQLdb

conn = MySQLdb.connect(host='localhost',port=3306,user='root',db='python2',passwd='czp8852887',charset='utf8')
#以dict的形式打印
curs = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
curs.execute('select * from test6')
print curs.fetchall()









































