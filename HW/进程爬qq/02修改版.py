import urllib.request
import re
from multiprocessing import Process
from multiprocessing import Queue
from time import sleep


# def putqueue(i):
#     crawlerQQ(i)
def crawlerQQ(i):

        list1 =[]
        url = "http://bbs.tianya.cn/m/post-140-393974-"+str(i)+"."+"shtml"
        response = urllib.request.urlopen(url)
        strData = response.read().decode("utf-8")
        qqPartern = re.compile("[Qq]{2}" ,re.I)
        numPartern = re.compile("[1-9]\\d{4,10}")
        resq = qqPartern.findall(strData)
        resu = numPartern.findall(strData)
        for j in range(len(resq)):
            if resq:
                res = resq[j]+":" + resu[j]
                list1.append(res)
        queue.put(list1)
        print(list1)

if __name__ == '__main__':
    # 创建一个队列，可以存放无限个数据
    queue = Queue()
    for i in range(0,50):
        # 创建一个父进程，并把队列传给子进程
        processFunc = Process(target=crawlerQQ, args=(i,))
        processFunc.start()

    while True:

        # 判断队列是否为空
        if queue.empty():
            print("该队列没有数据")
            sleep(1.5)
        else:
            data = queue.get()
            # print(data)
            sleep(1.5)

