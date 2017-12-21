'''
加强模式
'''

# 读入加强模式
def readPlusMode():
    file = open("./doc/4.txt", mode="r+", encoding="utf-8")
    print("读入之前文件指针的位置:", file.tell())  # 返回文件指针的位置
    print(file.read())
    print("读入之后文件指针的位置:", file.tell())  # 返回文件指针的位置
    file.write("fuck off")
    print("写出之后文件指针的位置：", file.tell())  # 返回文件指针的位置
    file.close()

# 覆写加强模式
def writePlusMode():
    file = open("./doc/4.txt", mode="w+", encoding="utf-8")
    print("文件打开了，文件的内容是：", file.read())
    print("准备写出，当前的文件指针位置是：", file.tell())
    file.write("fuck off and enjoy yourself")
    print("写出完毕，当前的文件指针位置是：", file.tell())
    print("写完立即读的结果是：", file.read())
    file.seek(0)  # 把指针拨回文件开头
    print("回拨指针后读的结果是：", file.read())
    file.close()

# 追加加强模式
def appendPlusMode():
    file = open("./doc/4.txt", "a+", encoding="utf-8")
    print("打开了，文件指针在", file.tell())
    file.write("\nyes sir!")
    print("追加完毕，文件指针在", file.tell())
    file.seek(0)
    print(file.read())
    file.close()


appendPlusMode()


# writePlusMode()
# readPlusMode()