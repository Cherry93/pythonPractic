'''
文件主要操作函数
'''


def mainFunctions():
    file = open("./doc/4.txt", "r+", encoding="utf-8")
    print(file.read(10))  # 读入两个字符（而不是指针位置）
    file.seek(0)
    print(file.readline())
    print(file.readline())
    print(file.readline())
    file.seek(0)
    print(file.readlines())
    file.writelines(["fuck\n", "shit\n", "damn\n"])
    file.close()

def truncateFile():
    file = open("./doc/5.txt", "r+", encoding="utf-8")
    # file.seek(32)
    print(file.readline())
    print(file.readline())
    file.seek(file.tell())  # 需要显式地拨动指针
    file.truncate()
    file.close()

def truncateFileII():
    file = open("./doc/5.txt", "r+", encoding="utf-8")
    file.truncate(64)
    file.close()

# truncateFileII()
# truncateFile()
# mainFunctions()