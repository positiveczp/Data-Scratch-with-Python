#-*-coding:utf-8-*-
import MySQLdb

conn = MySQLdb.connect(host='127.0.0.1',port=3306,user='root',db='python2',passwd='czp8852887',charset='utf8')
curs = conn.cursor()
#如果没有数据库，需要先创建
#curs.execute("create database if not exists python2")
#conn.select_db('python2')
#创建table
#curs.execute("create table if not exists test6(id int,info varchar(20))")
value = [1,'hi rollen']
curs.execute("insert into test6 values(%s,%s)",value)

values = []
for i in range(20):
    values.append((i,'hi rollen'+str(i)))
#分别执行插入，更新和删除
curs.executemany("insert into test6 values(%s,%s)",values)
curs.execute('update test6 set info="I am rollen" where id=3')
curs.execute('delete from test6 where id=10')
conn.commit()
curs.close()
conn.close()








