import threading

# 在python语言中,如果想要程序满负荷运行, 只会占用  1/count  左右的资源
# 在C语言,java语言 是可以达到满负荷的
# 要想使python满负荷运行,使用 进程 + 线程的方式



def func():
    while True:
        print("我要消耗你的资源")

if __name__ == '__main__':
    thread1 = threading.Thread(target=func)
    thread2 = threading.Thread(target=func)
    thread3 = threading.Thread(target=func)
    thread4 = threading.Thread(target=func)
    thread5 = threading.Thread(target=func)
    thread6 = threading.Thread(target=func)
    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()
    thread5.start()
    thread6.start()
    thread1.join()
    thread2.join()
    thread3.join()
    thread4.join()
    thread5.join()
    thread6.join()


