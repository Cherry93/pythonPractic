# 生成器

# 相似: 生成式列表
# list1 = [i for i in  range(1,10001)]

# 生成器--生成器表达式

# 创建一个生成器,
# 注意用 () 将生成式括起来会生成一个 生成器 即generator,  用[] 将生成式括起来会生成一个列表
genertor1 = (i for i in range(1,101))
print(genertor1)
print(type(genertor1))

# 获取genertor中的元素,通过next可以不断的获取下一个元素
genertor2 = (i for i in range(0,5))
# print(next(genertor2))
# print(next(genertor2))
# print(next(genertor2))
# print(next(genertor2))
# print(next(genertor2))

# 当genertor 指向最后一个元素时,继续读取下一个元素,程序会抛StopIteration 异常
# print(next(genertor2))

# 一般可以使用for循环来遍历genertor中的每一个元素
# for循环遍历genertor时不会抛出StopIteration异常, 当genertor迭代完之后会自动结束该for循环,或者return可以终止
# for i in genertor2:
#     print(i)

#一般的函数都是至上而下,立即执行的
# def func1():
#     print("a")
#     print("b")
#     print("c")
#     print("d")
#     print("e")

# 生成器--->生成器函数
def func1():
    print("a")
    yield
    print("b")
    yield
    print("c")
    yield
    print("d")
    yield
    print("e")
    yield

# 执行一下
# 函数中加yield的函数是生成器函数,
# 调用之后返回一个生成器genertor
genertor3 = func1()
# print(genertor3)
# print(type(genertor3))

# 使用next一步一步的执行
# next(genertor3)
# 模拟条件
# next(genertor3)
# 模拟条件
# next(genertor3)
# next(genertor3)
# next(genertor3)
# next(genertor3)

# for i in genertor3:
#     pass

def func2():
    for i in range(1,100):
        print(i)
        yield
genertor4 = func2()
next(genertor4)
next(genertor4)
next(genertor4)





















