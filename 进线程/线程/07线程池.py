# 导入线程池模块
import threadpool
import time

def eat(name):
    print("%s吃了我的奶酪"%name)
    time.sleep(2)

if __name__ == '__main__':
#    创建一个线程池
#    参数1: 用来设置线程的大小
    thPool =threadpool.ThreadPool(2)
    # 创建多个子线程请求
    # 参数1,子线程需要执行的函数的函数名
    # 参数2,用来设置传递给每个线程的参数,是一个列表
    nameList = ["啊猫","啊狗","啊毛","啊安培","啊啊","啊鸡","啊鸭"]
    # 返回装有了多个子线程请求的列表
    requestList = threadpool.makeRequests(eat,nameList)

#    将每个子线程的请求放入到线程池中去
#     for req in requestList:
#         thPool.putRequest(req)
    [thPool.putRequest(req) for req in requestList]
#   启动,  并等待所有的子线程执行完,
#   所有子线程执行完之后,才会执行 wait()后面的代码
    thPool.wait()
    print("主线程结束")





