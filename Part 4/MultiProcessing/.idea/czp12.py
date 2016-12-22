#-*-coding:utf-8-*-
import threading

def run(n):
    con.acquire()
    con.wait()
    print("run the thread: %s" % n)
    con.release()

if __name__ == '__main__':

    #获取Condition锁
    con = threading.Condition()
    for i in range(10):
        t = threading.Thread(target=run, args=(i,))
        t.start()

    while True:
        inp = input('>>>')
        if inp == "q":
            break
        #下面这三行是固定语法
        con.acquire()
        con.notify(int(inp))  #这个方法接收一个整数，表示让多少个线程通过
        con.release()













