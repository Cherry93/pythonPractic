# 问题: 如何实现多个子进程向主进程发送数据
# 解决: 将子进程处理完的数据放到队列中去,发送给主进程

from multiprocessing import Process
from multiprocessing import Queue
from time import sleep
import random

# 模拟一个子进程
def func(queue,number):
    print("第%d个进程开启了"%(number))
    #  模拟每个进程执行不同的时间
    sleep(random.randrange(4,10,2))
    # 将数据放到队列中去
    queue.put("第%d个进程结束了" % (number))
    # print("第%d个进程结束了" % (number))

if __name__ == '__main__':
    # 创建一个队列, 可以存放无限个数据
    queue = Queue()
#     模拟开启多个子进程
    for i in range(12):
        # 创建一个子进程,并把队列传给子进程
        processFunc = Process(target=func,args=(queue,i))
        processFunc.start()

#   主进程中需要一直从队列中取数据
    while True:
        # 判断队列是否为空
        if queue.empty():  #空
            print("该队列没有数据")
            sleep(0.5)
        else:
            data = queue.get()
            print(data)
            sleep(0.5)
















