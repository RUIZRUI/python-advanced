# -*- coding: utf-8 -*-

# threading.currentThread()  返回当前的线程变量
# threading.enumerate()   返回正在运行的线程的list
# threading.activeCount()  返回正在运行的线程数量 = len(threading.enumerate())


# Thread 类
# run()    表示线程活动
# start()  启动线程
# join([time])  等待至线程中止，阻塞调用线程直至线程的join() 方法被调用，可以加入时间
# isAlive()  线程是否是活动的
# getName()  返回线程名
# setName()  设置线程名

'''
    线程传参
        1. 元组 (参数1, 参数2,)
        2. 字典 {'参数': 参数1, '参数名': 参数2}
        3. 元组 + 字典 (参数1, 参数2,), {'参数': 参数3, '参数名': 参数4}
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
        print('开始线程: ' + self.name)
        print_time(self.name, self.counter, 5)
        print('退出线程: ' + self.name)

    
def print_time(threadName, delay, counter):
    while counter:
        time.sleep(delay)
        print(f'{threadName}: {time.ctime(time.time())}')
        counter -= 1

# 创建新线程
thread1 = myThread(1, 'Thread-1', 1)
thread2 = myThread(2, 'Thread-2', 2)

# 开启新线程
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print('退出主线程')