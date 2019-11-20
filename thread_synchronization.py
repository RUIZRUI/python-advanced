# -*- coding: utf-8 -*-

'''
    线程同步问题
''' 

import threading
import time

class myThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print('开启线程：' + self.name)
        # 获取锁
        threadLock.acquire()
        print_time(self.name, self.counter, 3)
        # 释放锁
        threadLock.release()


def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print(f'{threadName}: {time.ctime(time.time())}')
        counter -= 1


threadLock = threading.Lock()
threads = []

# 创建线程
thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)


# 开启新线程
thread1.start()
thread2.start()

# 添加线程到线程列表
threads.append(thread1)
threads.append(thread2)


# 等待所有线程完成
# join() 主线程任务结束之后，进入阻塞状态，一直等待其他的线程结束之后，主线程再终止
for t in threads:
    t.join()
print('退出主线程')