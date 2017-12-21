from threading import  Thread

# 注意: 进程与进程之间的内存空间是相互独立的
# 注意: 对于一个线程而言,该线程在那个进程就是使用的那个进程的内存空间,
# 多个线程在一个进程内,则这多个线程共享内存空间


number = 100
def func():
    global number
    number -= 10
    print("子线程number",number)
if __name__ == '__main__':
    print("主线程开始:",number)
    # func()
    threadFunc =Thread(target=func)
    threadFunc.start()
    print("主线程结束:", number)


