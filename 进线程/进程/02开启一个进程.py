from time import sleep
from multiprocessing  import Process

def createIphone8():
    while True:
        print("生产iphone8")
        sleep(1)


if __name__ == '__main__':
#     创建一个进程
    createProcess = Process(target=createIphone8)
#   启动该进程
    createProcess.start()

    #开启的进程在任务管理器是可见的,可以杀死,杀死的子进程不影响其他子进程

    # 注意:开启进程是一个消耗资源消耗性能的过程
    # 开启多个进程
    # createProcess2 = Process(target=createIphone8)
    # # 启动一个进程
    # createProcess2.start()

    while True:
        print("生产iphoneX")
        sleep(1.2)





