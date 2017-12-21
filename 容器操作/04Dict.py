'''
字典：键值对元素集
'''

# 创建字典
def createDict():
    # mdict = {
    #     'Name': 'john',
    #     'Age': 7,
    #     'Class': '1703',
    #     "hobby":["coding","reading","eating"],
    # }
    mdict = {}
    mdict["Name"] = "john"
    mdict["Age"] = 7
    mdict["rmb"] = 123.45
    mdict["isMale"] = True
    mdict["Class"] = "1703"
    mdict["hobby"] = ["coding", "reading", "eating"]
    print(mdict, type(mdict))

# 元素的访问
def visitItem():
    mdict = {
        'Name': 'john',
        'Age': 7,
        'Class': '1703',
        "hobby": ["coding", "reading", "eating"],
    }
    mdict["Name"] = "jack"
    mdict["Class"] = "深圳二院"
    print(mdict["Name"])
    print(mdict["Class"])
    # print(mdict["school"])#KeyError: 'school'

# 编辑和删除元素
def editItem():
    mdict = {
        'Name': 'john',
        'Age': 7,
        'Class': '1703',
        "hobby": ["coding", "reading", "eating"],
    }
    mdict["Name"] = "jack"  # 修改元素
    del mdict["Age"]  # 删除元素，再访问该键则会报错
    print(mdict)

# 遍历字典
def traverseDict():
    mdict = {
        'Name': 'john',
        'Age': 7,
        'Class': '1703',
        "hobby": ["coding", "reading", "eating"],
    }
    # 遍历所有的键
    # for item in mdict:
    #     print(item)
    # 遍历所有键值
    for k, v in mdict.items():
        print(k, v)

# 内建函数
def builtInFuncs():
    mdict = {
        'Name': 'john',
        'Age': 7,
        'Class': '1703',
        "hobby": ["coding", "reading", "eating"],
    }
    print(len(mdict))
    print(str(mdict), type(str(mdict)))

# 操作函数
def functions():
    mdict = {
        'Name': 'john',
        'Age': 7,
        'Class': '1703',
        "hobby": ["coding", "reading", "eating"],
    }
    # mdict.clear()#清空
    temp = mdict.copy()  # 拷贝形成独立副本
    temp["Age"] = 100
    print(temp)
    temp = mdict.keys()  # 返回键的“列表”
    print(temp, type(temp))  # dict_keys(['Name', 'Age', 'Class', 'hobby']) <class 'dict_keys'>
    print(list(temp))
    temp = mdict.values()  # 返回值的“列表”
    print(temp, type(temp))  # dict_keys(['Name', 'Age', 'Class', 'hobby']) <class 'dict_keys'>
    print(list(temp))
    # print(mdict.pop("Name"))#弹出并返回键的值
    # print(mdict.popitem())#弹出并以元组形式返回最后一个键值对
    # print(mdict.popitem())
    # print(mdict.popitem())
    # print(mdict.popitem())
    # print(mdict.popitem())#KeyError: 'popitem(): dictionary is empty'
    print(mdict.get("Name"))
    print(mdict.get("fuck"))  # 获取键的值，没有该键则返回默认值None
    print(mdict.get("shit", "fuck off"))  # 获取键的值，没有该键则返回默认值"fuck off"
    # print(mdict["shit"])
    # mdict.update(   {"Name":"smith","Age":100,"fuck":666}  )#以参数字典为基准，校正原字典
    # mdict.setdefault("school")
    mdict.setdefault("school", "未知院校")  # 怕你没school，果真没有就设置为"未知院校"
    mdict.setdefault("Name", "无名氏")
    print("\n")
    print(mdict.fromkeys(["fuck", "shit", "asshole"]))
    print(mdict.fromkeys(("fuck", "shit", "asshole"), "不知道"))  # 快速形成以("fuck","shit","asshole")中的元素为键，默认值为“不知道”的字典
    print(mdict.fromkeys("hello", "不知道"))
    # print(mdict)

# functions()