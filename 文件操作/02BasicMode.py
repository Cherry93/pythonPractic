'''
基本读写模式
'''


def readOnly():
    # 以只读模式（r），utf-8编码打开指定文件
    file = open("./doc/1.txt", mode="r", encoding="utf-8")
    content = file.read()  # 读入全部内容
    print(content, type(content))  # <class 'str'>
    # file.write("hello")#不支持写入
    file.close()  # 关闭文件流

# 覆写模式：打开时清空内容，只能写出不能读入
def writeMode():
    file = open("./doc/2.txt", mode="w", encoding="utf-8")
    print(type(file))  # TextIOWrapper
    file.write("hello")
    print(file.read())
    file.close()

# 追加模式，追加到文件末尾
def appendMode():
    file = open("./doc/2.txt", mode="a", encoding="utf-8")
    file.write("world")
    file.close()
    file = open("./doc/2.txt", mode="r", encoding="utf-8")
    print(file.read())
    file.close()

# 创写模式：强制打开一个并不存在的文件并开始写入
def extendMode():
    file = open("./doc/3.txt", mode="x", encoding="utf-8")
    file.write("hello world")
    file.close()


extendMode()
# appendMode()
# writeMode()
# readOnly()
