#-*-coding:utf-8-*-
import MySQLdb

try:
    conn = MySQLdb.connect(host='localhost',port=3306,user='root',db='python2',passwd='czp8852887',charset='utf8')
    curs = conn.cursor()
    count = curs.execute('select * from test6')
    print "there is %s rows record" %count

    result = curs.fetchone()
    print result
    print "ID: %s info %s" %result

    results = curs.fetchmany(5)
    for r in results:
        print r

    curs.scroll(0,mode='absolute')
    results = curs.fetchall()
    for r in results:
        print r[1]

    conn.commit()
    curs.close()
    conn.close()
except:
    print 'Error!'


































