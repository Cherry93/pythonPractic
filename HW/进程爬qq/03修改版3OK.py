import urllib.request
import re
from multiprocessing import Process
from multiprocessing import Queue
from time import sleep

def crawlerQQ(i):

    qqPattern = re.compile("[Qq]{2}")
#     正则表达式用来匹配qq号码
    qqNumberPattern = re.compile("[1-9]\d{4,11}")

#   创建一个空列表,用来存储qq号码
    qqNumberList = []


    urlPath = "http://bbs.tianya.cn/m/post-140-393974-"+ str(i) +".shtml"
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
    # print(qqNumberList)
    # queue.put(qqNumberList)
    return qqNumberList




def main(queue,i):

    qqNumerList = crawlerQQ(i)
    queue.put(qqNumerList)
#
# #     print(qqNumerList)
# #     print(len(qqNumerList))
# # #   去重
# #     listQQ = list(set(qqNumerList))
# #     # 排序
# #     listQQ.sort(key=qqNumerList.index)
# #     print(listQQ)
# #     print(len(listQQ))

if __name__ == '__main__':

    # 创建一个队列，可以存放无限个数据
    queue = Queue()
    for i in range(0,50):
        # 创建一个父进程，并把队列传给子进程
        processFunc = Process(target=main, args=(queue,i))
        processFunc.start()

    while True:

        # 判断队列是否为空
        if queue.empty():
            print("该队列没有数据")
            sleep(1.5)
        else:
            data = queue.get()
            print(data)
            sleep(1.5)




