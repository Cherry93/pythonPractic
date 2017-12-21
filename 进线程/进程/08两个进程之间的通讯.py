# 问题:  如何实现两个进程之间的通讯
# 解决:  可以用pipe  管道来连接两个进程
from multiprocessing import Process
from multiprocessing import Pipe

# 接收一个管道连接
def func(connection):
#     模拟一个子进程,可以接收,发送另外一个进程的数
#     pass
    print("子进程开启")
    # 接收主进程的数据
    recvData = connection.recv()
    print("接收到的数据:",recvData)
    # 发送数据给主进程
    connection.send("没我你不行的子进程")

    print("子进程结束")

if __name__ == '__main__':
#     创建一个管道,该管道可以实现进程与进程之间的通
#    创建后会 返回管道的两个连接端
    connectA,connectB= Pipe()
#     创建并启动一个进程
#     并把管道的另一端交给子进程
    processFunc = Process(target=func,args=(connectB,))
    processFunc.start()

#   发送数据
    connectA.send("来自伟大的主进程")
#   接收数据
    print("主进程接收到的数据:",connectA.recv())












