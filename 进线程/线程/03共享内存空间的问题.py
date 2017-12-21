

'''
注意: 当多个线程共享内存时,可能会导致数据错乱

# 问题:线程之间是同时执行的,可以操作同一个变量
     例: 线程1 执行了  number += 5  -- >number = 105
         假设跳到了线程2 , number += 8   --> number = 113
#        继续多次执行就会导致数据错作

          number += 5  其实做两件事情,先执行number + 5,并赋值给 临时变量, 然后将临时变量赋值给 number

    解决:  把需要操作变量的代码看作一个整体
        加锁:
        在操作该变量之前加锁

        在操作完改变量后解锁

    优缺点:
        优点:保证数据的完整性,准确性
        缺点: 会影响线程执行的效率
        一般不建议使用
    死锁: 当锁住的代码出现异常,会导致锁不能释放, 而另外一个线程可能一直在等待该锁的释放,就会造成死锁现象
   解决: 无论程序是否抛出异常都出执行  释放锁功能



'''
from threading import  Thread
import threading
# 创建一个锁
lock = threading.Lock()

number = 100
def func1():
    global number
    for i in range(1,10000000):
        # 加锁
        lock.acquire()
        number+= 5
        number -= 5
    #   释放锁
        lock.release()

    print("子线程1:",number)

def func2():
    global  number
    for i in range(1,10000000):
        lock.acquire()
        number  += 8
        number  -= 8
        lock.release()
    print("子线程2:",number)

if __name__ == '__main__':

    print("主线程开启:",number)
    threadFunc1 = Thread(target=func1)
    threadFunc2 = Thread(target=func2)
    threadFunc1.start()
    threadFunc2.start()
    threadFunc1.join()
    threadFunc2.join()
    print("主线程结束:", number)

