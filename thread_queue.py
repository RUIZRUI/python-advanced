# -*- coding: utf-8 -*-

'''
    线程优先级队列

    queue 模块：实现了同步、线程安全
        FIFO, LIFO, 优先级等

    queue.qsize()  队列大小
    queue.empty()  是否空
    queue.full()   是否满
    queue.full = maxsize
    queue.get([block, timeout])    获取队列
    queue.get_nowait() = queue.get(False)
    queue.put(item) 
    queue.put_nowait(item)  = queue.put(item, False)
    queue.task_done() 完成一项工作
    queue.join()  等待队列为空，在执行别的操作
'''

import queue
import threading
import time


exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, threadID, name, que):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.que = que

    def run(self):
        print('开始线程：' + self.name)
        process_data(self.name, self.que)
        print('退出线程：' + self.name)


def process_data(threadName, que):
    while not exitFlag:
        queueLock.acquire()
        if not workQueue.empty():
            data = que.get()
            queueLock.release()
            print(f'{threadName} processing {data}')
        else:
            queueLock.release()
        time.sleep(1)
        



threadList = ['Thread-1', 'Thread-2', 'Thread-3']
nameList = ['One', 'Two', 'Three', 'Four', 'Five']
queueLock = threading.Lock()
workQueue = queue.Queue(10)
threads = []
threadID = 1

# 创建线程
for tName in threadList:
    thread = myThread(threadID, tName, workQueue)
    thread.start()
    threads.append(thread)
    threadID += 1


# 填充队列
queueLock.acquire()
for word in nameList:
    workQueue.put(word)
queueLock.release()


# 等待队列为空
while not workQueue.empty():
    pass


# 通知线程退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print('退出主线程')


'''
    三个线程退出：
        1. 一个先退出，另外两个隔一秒退出
        2. 两个先退出，另一个隔一秒再退出
        3. 三个立即一起退出
'''