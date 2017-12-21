'''
步骤:
    1.导入线程的模块
    2.创建一个线程
    3.启动一个线程


# 线程是最小的执行单元:
     代码是在线程中执行的
# 主线程的名字就是 MainThread


'''
from threading import Thread
import threading

# def func():
#     print("启动了一个子进程")

def func(name,food):
    # 获取子线程的名字
    print("子线程的名字:",threading.currentThread().getName())

    # print("启动了一个子进程")
    print("%s是%s刚交的朋友"%(name,food))

if __name__ == '__main__':
    # 可以获得当前线程的名字
    print("主线程的名字%s:",threading.currentThread().getName())


    # 创建一个thread
    # target用来指定目标函数的函数名
    # threadFunc = Thread(target=func)
    # args用来传递参数, args是元组的形式,可以传递多个参数
    # threadFunc = Thread(target=func,args=("金三胖胖","奥巴马"))
    # kwargs是用来传递 key-value形式的参数, kwargs是字典的形式, 可以用来传递多个参数
    # threadFunc = Thread(target=func,kwargs={"food":"奥把马","name":"金三胖胖"})

    #可以给子进程指定名字,
    # name参数用来指定该线程的名字
    threadFunc = Thread(target=func,kwargs={"food":"奥把马","name":"金三胖胖"},name="funcThread")
#
#   启动子进程
    threadFunc.start()





