from time import sleep
from multiprocessing import Process
import os

def createIphone8():
    print("当前进程的id:%d"%(os.getpid()))
    # while True:
    sleep(1)
    print("生产iphone8")
if __name__ == '__main__':
    # 获取进程的id,用来区分进程
    # os.getpid()在那个进程中就获得该进程的id
    print("父进程id:%d"%(os.getpid()))

    iphone8Process = Process(target=createIphone8)
    iphone8Process.start()
    # 子进程调用join()后,表示需要该子进程执行完之后再去执行父进程,
    iphone8Process.join()
    # join后面的代码会在该子进程结束后才执行
    print("主进程结束了")

    # while True:
    #     sleep(1.2)
    #     print("生产iphoneX")

'''
# 进程之间的代码是没有关系
# 严格意义来讲在执行顺序上是没有关系

# 进程的分类:
    主进程: 当程序启动的时候,默认(第一个)启动的那个进程就是主进程
        一般主进程用来管理,协调,调用子进程
    子进程: 通过父进程开启的进程就是该父进程的进程子进程
        一般来处理一个子功能, 或者耗时,消耗资源的功能

'''









