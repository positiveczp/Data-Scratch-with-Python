#-*-coding:utf-8-*-

import multiprocessing,random
from multiprocessing import freeze_support
from multiprocessing.managers import BaseManager

#发送任务的队列
task_queue = multiprocessing.Queue()
#接受结果的队列
result_queue = multiprocessing.Queue()
#从BaseManager继承的QueueManager
class QueueManager(BaseManager):
    pass
#未解决__main__.<lambda>not found问题
def get_task_queue():
    return task_queue
#未解决__main__.<lambda>not found问题
def get_result_queue():
    return result_queue

#把两个Queue都注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue',callable=get_task_queue)
QueueManager.register('get_result_queue',callable=get_result_queue)
#绑定端口5000，设置验证码'abc'
manager = QueueManager(address=('127.0.0.1',5000),authkey='abc')

def communicate():
    #获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()
    #放几个任务进task队列
    for i in range(10):
        n = random.randint(0,10000)
        print 'put task %d...' %n
        task.put(n)
    #从result队列读取结果
    print 'try get results...'
    for i in range(10):
        r = result.get(timeout=10)
        print 'result: %s' %r
    #关闭
    manager.shutdown()

if __name__=='__main__':
    freeze_support()
    manager.start()
    communicate()




