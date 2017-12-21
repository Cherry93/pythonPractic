import threading

# 创建一把锁
lock = threading.Lock()

#规范
# 方式1:
def eat():
    try:
        lock.acquire()
        #   模拟一段需要加锁的代码,可能出现异常
        print("模拟一段需要加锁的代码")
    except:
        pass
    finally: #finally无论是否出现异常都执行finally
#        释放锁
        lock.release()

#方式2: with自动释放
def eat2():
    with lock:
        # 该代码可能出现异常
        print("模拟一段需要加锁的代码,")







