'''
使用装饰器查看函数运行的时间，有什么作用
'''
import time

def exeTime(func):
    def newFun(*args,**kwargs):
        t0 = time.time()
        print(t0)
        back = func(*args,**kwargs)
        t1 = time.time()
        print(t1)
        print(t1 - t0)
        return back
    return newFun
@exeTime
def funTest():
   for i in range(10000000):
       pass
funTest()