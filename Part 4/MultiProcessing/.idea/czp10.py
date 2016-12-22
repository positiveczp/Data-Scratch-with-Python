#-*-coding:utf-8-*-
import time
import threading

def run(n):
    semaphore.acquire()
    print 'run the thread: %s\n' %n
    time.sleep(5)
    semaphore.release()

num = 0
#信号量锁
semaphore = threading.BoundedSemaphore(5) #最多允许5个线程同时运行
for i in range(20):
    t = threading.Thread(target=run,args=(i,))
    t.start()



















