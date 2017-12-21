import urllib.request
import re
from multiprocessing import Process
from multiprocessing import Queue
from time import sleep
from multiprocessing.pool import Pool
import random




# 爬取社区的qq号
# def crawlerQQ(urlPath):
def crawlerQQ(queue,i):

#     urllib去请求(下载)网页
#     读取一行数据
#     在该行找到是否有 qq/QQ/qQ/Qq 字符
#     在在该行找到qq号码,
#     存起来

#     requestQQ = urllib.request.urlopen(urlPath)
#     lines = requestQQ.readlines()
#     for line in lines:

#    正则表达式用来匹配 "qq,QQ..." 等字符
#     qqPattern = re.compile("qq",re.I)
    qqPattern = re.compile("[Qq]{2}")
#     正则表达式用来匹配qq号码
    qqNumberPattern = re.compile("[1-9]\d{4,11}")

#   创建一个空列表,用来存储qq号码
    qqNumberList = []
    #将数据放到队列中去


    urlPath = "http://bbs.tianya.cn/m/post-140-393974-" + str(i) + ".shtml"
#   请求数据拿到每一行数据
    for line in urllib.request.urlopen(urlPath):
        line = line.decode("utf-8")
    #         在该行找到qq字符
        resQQ = qqPattern.findall(line)
    #       判断该行是否有qq号
        if len(resQQ) != 0: #找到qq字符
    #            继续寻找该行的qq号
            qqNumberRes = qqNumberPattern.findall(line)
                # print(qqNumberRes)
                # 从结果中获取每一个qq号
            for qqNumber in qqNumberRes:
                qqNumberList.append(qqNumber)


    queue.put(qqNumberList)
    # print(qqNumberList)

    return  qqNumberList





# def main():
#
#     # qqNumerList = crawlerQQ("http://bbs.tianya.cn/m/post-140-393974-6.shtml")
#     qqNumerList = crawlerQQ()
#     print(qqNumerList)
#     print(len(qqNumerList))
# #   去重
#     listQQ = list(set(qqNumerList))
#     # 排序
#     listQQ.sort(key=qqNumerList.index)
#     print(listQQ)
#     print(len(listQQ))

if __name__ == '__main__':
    processPool = Pool(4)
    # 创建一个队列，可以存放无限个数据
    queue = Queue()
    for i in range(1, 50):
        # 创建一个父进程，并把队列传给子进程
        # processFunc = Process(target=crawlerQQ, args=(queue, i))
        # processFunc.start()
        processPool.apply_async(func=crawlerQQ, args=(queue, i))
    processPool.close()
    #join用来等待子进程执行结束后,在执行join后的代码,进程池使用join时,需要先执行close
    processPool.join()

    while True:

        # 判断队列是否为空
        if queue.empty():
            print("该队列没有数据")
            sleep(0.5)
        else:
            data = queue.get()
            print(data)
            sleep(0.5)

    # main()



