#-*-coding:utf-8-*-
import threading
from random import randint
from time import sleep, ctime

L = threading.Lock()  # 引入锁


def hi(n):
    L.acquire()  # 加锁
    for i in [1, 2]:
        print(i)
        sleep(n)
        print("ZzZzzz, sleep: ", n)
    L.release()  # 释放锁


def main():
    print "### Start at: ", ctime()
    threads = []

    for i in range(10):
        rands = randint(1, 2)
        t = threading.Thread(target=hi, args=(rands,))
        threads.append(t)

    for i in range(10):
        threads[i].start()

    for i in range(10):
        threads[i].join()

    print "### Done at: ", ctime()


if __name__ == '__main__':
    main()