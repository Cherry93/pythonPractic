# 延时线程
from threading import Timer

def  func():
    print("林志玲姐姐叫你起床")

if __name__ == '__main__':
#    创建一个延时线程
#   参数1,表示延迟多长时间后执行, 单位是秒
#   参数2,目标函数名
    timerF = Timer(3,func)
#   启动
    timerF.start()











