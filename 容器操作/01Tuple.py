'''
元组：有序、可重复、只读元素集
'''

# 创建元组
def createTuple():
    mtup = ()
    mtup = ("Google",)
    # mtup = ("Google",123,45.6,False)
    mtup = 1, 2, 3
    print(mtup, type(mtup))

# 访问元组中的元素
def visitItem():
    mtup = (0, 1, 2, 3, 4, 5)
    print(mtup[3])#访问下标为3的元素

    # 遍历所有元素
    for item in mtup:
        print(item)

# 删除元组
def deleteTuple():
    mtup = (0, 1, 2, 3, 4, 5)
    # 不能编辑元素
    # mtup[3] = "1234"#TypeError: 'tuple' object does not support item assignment
    del mtup  # 从内存中销毁mtup
    print(mtup)  # 系统提示该变量未定义：NameError: name 'mtup' is not defined

# 元组相加，合并为一个大元组，继承原来的顺序
# 元组 * N 将元组元素重复N遍，形成新元组
# item in mtup 判断mtup元组中是否含有item这个元素
# 和字符串操作符基本一样
def operands():
    mtup1 = (0, 1, 2)

    # mtup2 = (3,4,5)
    # temp = mtup1  + mtup2

    # temp = mtup1 * 10
    # print(temp, type(temp))

    print(2 in mtup1)

# 元组截取
# mtup[start:end:step]
# mtup[开始下标:结束下标:步长]
# 含头不含尾（结束下标本身不能被包含进去）
def subTuple():
    mtup = (0, 1, 2, 3, 4, 5)
    print(mtup[1:4])
    print(mtup[0:5:2])
    print(mtup[:])
    print(mtup[::2])
    print(mtup[5:0:-2])
    print(mtup[5::-1])

# 相关函数
def functions():
    # mtup = (-5,0,1,5,2,3)
    # print("元组的长度为",len(mtup))
    # print(max(mtup))
    # print(min(mtup))
    # print(sum(mtup))#求和
    # mtup2 = ("a","b","c","中国","美帝")
    # print(max(mtup2))
    # print(min(mtup2))
    # 将其他类型强制转换为元组类型
    temp = tuple("hello")
    temp = tuple(["张三", 123, 45.6])
    print(temp, type(temp))


# functions()
# subTuple()
# operands()
# deleteTuple()
createTuple()
# visitItem()
