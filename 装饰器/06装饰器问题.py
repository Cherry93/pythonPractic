# 支付宝 ---->滴滴打车,口碑么,共享单车,携程,.....
# 淘宝---> 登陆,注册

# def func1():
#     print("基础功能1")
#
# def func2():
#     print("基础功能2")
#
# def func3():
#     print("基础功能3")

# 以上基础功能会被多个地方调用多次
# 模拟
# func1()
# func2()
# func3()

# 项目经理1: 滚
# 验证1
# 验证2
# 验证3
# func1()

# 验证1
# 验证2
# 验证3
# func2()

# 项目经理2:  今天你去财务室结账吧
# def func1():
#     # 验证1
#     # 验证2
#     # 验证3
#     print("基础功能1")
#
# def func2():
#     # 验证1
#     # 验证2
#     # 验证3
#     print("基础功能2")
#
# def func3():
#     # 验证1
#     # 验证2
#     # 验证3
#     print("基础功能3")




# 项目经理4: 下周开始工资减半
# def check():
# # 验证1
# # 验证2
# # 验证3
#     pass
#
# def func1():
#     check()
#     print("基础功能1")
#
# def func2():
#     check()
#     print("基础功能2")
#
# def func3():
#     check()
#     print("基础功能3")

# 希望在不改变原有代码的基础上给一个函数添加新的功能
def func1():
    print("基础功能1")

def func2():
    print("基础功能2")

def func3():
    print("基础功能3")

# def outter():
#     print("模拟需要添加的新功能")
#     func3()

# def outter(func):
#     print("模拟需要添加的新功能")
#     func()

# outter ---func1
def outter(func):
    def inner():
        print("模拟需要添加的新功能")
        func()
    return inner

# inner = outter(func1)
# inner()
# func1 --> inner
func1 = outter(func1)
func1()
















