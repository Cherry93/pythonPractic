# @Author  : Crown
# @Time    : 2017/11/29 12:39
# @File    : decorator.py

# 修饰器
import time


def timmer(func):
    def warpper(*args, **kawargs):
        start_time = time.time()
        func()
        stop_time = time.time()
        print('the func run time is %s' % (stop_time - start_time))

    return warpper


@timmer
def test1():
    time.sleep(3)
    print('in hte test1')


test1()

# @Author  : Crown
# @Time    : 2017/11/29 14:44
# @File    : decorator3.py


import time


def timmer(func):  # func=test1
    def deco(*args,**kwargs):
        start_time = time.time()
        func(*args,**kwargs)
        end_time = time.time()
        print('the func run time is %s' % (end_time - start_time))

    return deco


@timmer
def test1(arg,arg2):
    time.sleep(2)
    print('in the test1',arg,arg2)


@timmer  # 相当于test2=timmer(test1)
def test2():
    time.sleep(2)
    print('in the test2')


# test1=timmer(test1)

test1("Alex","呵呵")
test2()