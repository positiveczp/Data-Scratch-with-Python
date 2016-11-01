#-*-coding:utf-8-*-
import MySQLdb
conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',db='python2',passwd='czp8852887',charset='utf8')
curs = conn.cursor()

#sql = "create table test7(firstname char(20),lastname char(20),age int,sex char(1),income float)"
#curs.execute(sql)
sql = "insert into test7(firstname,lastname,age,sex,income)values('陈','梓平哈哈',3,'m',20000)"
try:
    curs.execute(sql)
    conn.commit()

except:
   conn.rollback()

curs.close()
conn.close()
































