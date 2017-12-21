'''
列表：有序、可重复元素集
'''


# 列表创建
def createList():
    # 简单创建
    # mlist = []
    # mlist = ["hello",123,45.67,False]
    # 推导式创建
    # temp ="zhagnsan" if 1+1>2 else "lisi"
    mlist = [c for c in "hello"]
    mlist = [c + "%" for c in "hello"]
    mlist = [c + "%" for c in "hello" if (c in ("a", "b", "c", "d", "e", "f", "g"))]
    print(mlist, type(mlist))


# 访问列表元素
def visitItem():
    mlist = ["apple", "microsoft", "google", "tencent"]
    # print(mlist[0])
    # print(mlist[1])
    # print(mlist[2])
    # print(mlist[3])
    for item in mlist:
        print(item)


        # createList()


# visitItem()

# 编辑列表元素
def editList():
    mlist = ["apple", "microsoft", "google", "tencent"]
    mlist[0] = "banans"  # 修改元素
    del mlist[3]  # 删除下标为3的元素
    print(mlist)


# 列表操作符
def operands():
    mlist1 = ["apple", "microsoft", "google", "tencent"]
    mlist2 = ["huawei", "baidu", "alibaba"]
    print(mlist1 + mlist2)
    # print(mlist2 * 2)
    print("千锋" in mlist1)
    print("千锋" in (mlist1 + mlist2))


# 列表截取
def subList():
    mlist = ['apple', 'microsoft', 'google', 'tencent', 'huawei', 'baidu', 'alibaba']
    temp = mlist[1:6]
    temp = mlist[1:len(mlist)]
    temp = mlist[::-1]
    temp = mlist[len(mlist) - 1:0:-2]
    print(temp)


# 列表的嵌套
def nestedList():
    mlist1 = ["apple", "microsoft", "google", "tencent"]
    mlist2 = ["huawei", "baidu", "alibaba"]
    nlist = [mlist1, mlist2]
    nlist.append("shit")
    print(nlist)
    print(nlist[0][3])


# 列表操作的内建函数
def builtInFunctions():
    mlist1 = ["apple", "microsoft", "google", "tencent"]
    mlist2 = [i for i in range(11)]
    print(len(mlist1))
    print(max(mlist1))
    print(min(mlist1))
    print(sum(mlist2))
    print(list("hello"))
    print(list((1, 2, 3)))

# 列表的操作函数
def functions():
    mtup = [i for i in range(10) if i % 2 == 0]
    # mtup.append(10)#追加元素
    # mtup.clear()#清空列表
    temp = mtup.copy()  # 复制形成一个独立的副本
    temp[0] = "shit"
    # mtup += [2,2,2]
    print(mtup.count(2))  # 数一数2出现的次数
    # mtup.extend(  ["hello","welcome"] )#拓展列表，其参数是一个【可迭代对象】（容器、字符串等你），向列表中追加其中的所有元素
    # mtup.extend(    ("hello","welcome") )
    # mtup.extend(  "hello" )
    # print(temp)
    # [0,2,4,6,8]
    print(mtup.index(6, 2, 4))  # 在下标2-4的范围内检索元素6出现的下标
    mtup.insert(2, "shit")  # 在下标2的元素前面插入“shit”
    # item = mtup.pop()#弹出并返回最后一个元素
    item = mtup.pop(-2)  # 弹出并返回指定下标的元素（此处为倒数第二个元素）
    print(item)
    mtup = [0, 2, "4", 6, 8, "4"]
    mtup.remove("4")  # 移除第一个出现的“4”
    mtup = [0, 2, 4, 6, 8]
    mtup.reverse()  # 翻转列表
    print(mtup)
    mtup = [7, 0, 9, 2, 5, 3, 4, 6, 8, 1]
    # mtup.sort()
    mtup.sort(reverse=True)  # 列表排序，reverse选择升序或降序
    print(mtup)

# 组合遍历、反向遍历、带序号的遍历
def traverseSkills():
    labels = ["最有钱的公司", "比尔的公司", "邪恶的公司", "擅长拷贝的公司"]
    companies = ["apple", "microsoft", "google", "tencent"]
    # for x in companies:
    #     print(x)

    # 组合遍历多个等长的列表
    # for l,c in zip(labels,companies):
    #     # print(l,c)
    #     # print("宇宙间%s是%s"%(l,c))
    #     print("宇宙间{1}是{0}".format(l,c))

    # 使用reversed(iterable)实现反向遍历
    # for i in reversed(companies):
    #     print(i)

    # 使用enumerate(iterable)实现序号-元素形式的遍历
    for i,c in enumerate("hello"):
        print(i,c)


traverseSkills()


