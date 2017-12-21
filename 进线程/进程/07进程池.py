'''
问题: 理论上进程数量越多,执行效率越高, 但是进程的开启,运行,切换时消耗资源消耗性能
      所以需要找到一个效率最高的点,  当进程的数量小于等于cpu的核心数时效率最高
#   1,2,3,.........50
解决: 1.如果进程数小于cpu核心数,直接运行
      2.如果进程数大于cpu核心数,最多同时开启cpu核心数个进程
#   进程池:  可以限制进程同时运行的数量,  如果有50个进程,可以设置进程池的数量为cpu的核心数(假设是4),当进程池开启
             时,会按照队列顺序,现执行前4个进程,其他进程处于等待状态, 当进程池中的某个进程执行完后,排在队列前面的进程
             就会执行, ...

            数据结构; 列队, 栈
'''
import os
from time import  sleep
from multiprocessing.pool import Pool
import random

#模拟一个子进程
def funct(number):
    print("进程编号:%d,当前进程id:%d"%(number,os.getpid()))
    # sleep(3)
    sleep(random.randrange(5,10,2))
    print("进程编号:%d,结束id:%d" % (number, os.getpid()))

if __name__ == '__main__':
    print("主进程id:%d"%(os.getpid()))

#   创建一个进程池
#    参数用来设置进程池中可以最多同时运行的进程数量
#   默认(空参)情况,进程池设置的进程数量是当前cpu的核心数
    processPool = Pool(4)

#   同步:代码在一个进程中至上而下的执行
#   异步: 当一个进程开启了另外一个进程(子进程),子进程与该进程执行顺序互不影响,就是异步
    #   模拟多个进程
    for i in range(12):
#       向进程池中添加子进程
#       func指定的是子进程需要执行的函数名
#       args是用来传递给子进程的参数
        processPool.apply_async(func=funct,args=(i,))
#   让进程池启动
#   colse必须在join前面执行,
    processPool.close()
    #join用来等待子进程执行结束后,在执行join后的代码,进程池使用join时,需要先执行close
    processPool.join()
    print("主进程结束id:%d" % (os.getpid()))








