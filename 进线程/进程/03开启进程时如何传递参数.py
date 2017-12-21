from multiprocessing import  Process

# def  func(*args,**kwargs)

# def eat(name):
#     print("%s吃茶叶蛋"%(name))

def eat(name,food):
    print("%s请奥巴马吃%s"%(name,food))

if __name__ == '__main__':
#    创建一个进程
#     args用来传递参数给进程需要执行的函数,   args需要是元组类型的参数
#     processEat = Process(target=eat,args=("金三胖胖",))
#     processEat = Process(target=eat,args=("金三胖胖","6块钱的麻辣烫"))
#    kwargs 用来传递key-value形式的的参数, kwargs 需要的是字典形式的参数
    processEat = Process(target=eat,kwargs={"food":"德芙","name":"安培金山" })
#     启动进程
    processEat.start()






