import threading

'''
threadLocal(c,python,java)
使用threadlocal,可以为每一个使用threadLocal的线程创建一个内存副本, 操作该内存副本不会影响其他的线程
'''

# 创建一个threadlocal
threadlocal = threading.local()


def eat(name):
    print("%s 吃了我的奶酪"%(name))
#   把需要创建内存副本的变量设置给 threadLocal
    threadlocal.name  = name
    getName()

def getName():
    print("获取threadlocal中的变量:",threadlocal.name)



if __name__ == '__main__':
    name = "奥巴马"
    # name = [1,2,3]
    thread1 = threading.Thread(target=eat,args=("奥宝马",))
    thread2 = threading.Thread(target=eat,args=("金三胖胖",))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()


