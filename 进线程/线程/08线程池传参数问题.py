import threadpool
import time

def eat(a,b,c):
    print("%s请%s吃%s"%(a,b,c))
    time.sleep(2)

if __name__ == '__main__':
    # 设置参数
    # 方式1: 相当于args
    # list1 = [1,2,3]
    # list2 = [4,5,6]
    # list3 = [7,8,9]
    # list4 = [11,55,66]
    # argsList = [(list1,None),(list2,None),(list3,None),(list4,None)]

    # 方式2: 相当于kwargs
    dict1 = {"c":3,"b":2,"a":1}
    dict2 = {"c":4,"b":3,"a":2}
    dict3 = {"c":5,"b":4,"a":3}
    dict4 = {"c":6,"b":5,"a":4}
    # args,kwargs
    argsList = [(None,dict1),(None,dict2),(None,dict3),(None,dict4)]


    thPool = threadpool.ThreadPool(2)
    requestList = threadpool.makeRequests(eat,argsList)
    [thPool.putRequest(req) for req in requestList]

    thPool.wait()

