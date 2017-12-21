'''
集合：无序、不重复元素集
'''


# 创建列表
def createSet():
    # mset = {}#不能这样创建，{}代表一个空字典
    mset = set()  # 创建空集合
    mset = {'google', 'microsoft', 'apple', 'alibaba', 'tencent', 'baidu'}
    mset = {c for c in "hello"}  # 推导式
    print(mset, type(mset))

# 遍历集合
def traverseSet():
    mset = {'google', 'microsoft', 'apple', 'alibaba', 'tencent', 'baidu'}
    for c in mset:
        print(c)


        # createSet()

# 集合的操作符
def operands():
    mset1 = {'google', 'microsoft', 'apple', 'alibaba', 'tencent', 'baidu'}
    mset2 = {'alibaba', 'tencent', 'baidu', 'huawei', 'xiaomi', 'qianfeng'}
    print("apple" in mset1)
    print(mset1 & mset2)  # 交集
    print(mset1 | mset2)  # 并集
    print(mset1 - mset2)  # 1有2无
    print(mset1 ^ mset2)  # 仅1+仅2

# 相关函数
def functions():
    mset1 = {'google', 'microsoft', 'apple', 'alibaba', 'tencent', 'baidu'}
    print(len(mset1))
    print(max(mset1))
    print(min(mset1))
    mset = {i for i in range(1, 11)}
    print(sum(mset))
    print(set("hello"))
    print(set([1, 2, 3, 4, 5]))
    print(set((1, 2, 3, 4, 5)))
    mset = {"f", "c", "a", "g", "d", "b", "e"}
    print(mset)
    print(sorted(mset), type(sorted(mset)))  # 形成排序后的列表
    print(mset)
    # operands()
    # traverseSet()

functions()
