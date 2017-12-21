from multiprocessing import Process

number = 100

def edterNumber():
    global number
    number = number - 10
    print("子进程中的:",number)

if __name__ == '__main__':
    print("主进程开始时:",number)
    # edterNumber()
    processE = Process(target=edterNumber)
    processE.start()
    processE.join()
    print("主进程结束时:", number)
# 注意: 进程之间的变量是互不影响的, 当通过父进程开启一个主进程时,
# 子进程会开辟自己独立的内存空间,并将父进程中的变量值拷贝过来







