from multiprocessing import  Process

# def  func(*args,**kwargs)

# def eat(name):
#     print("%s吃茶叶蛋"%(name))

def eat(name,food):
    print("%s请奥巴马吃%s"%(name,food))

if __name__ == '__main__':
#    创建一个进程

    # 注意:  target指定的是需要在进程中执行的 函数  名  ,不能是函数名(), 这种形式表示的是调用,会返回函数执行完的结果, 而不是函数本身
    processEat = Process(target=eat,kwargs={"food":"德芙","name":"安培金山" })
#     启动进程
    processEat.start()