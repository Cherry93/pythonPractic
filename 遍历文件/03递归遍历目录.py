import os

# 递归遍历目录

def  getAllDirAndFile(targetPath):
#     获取到该目录下的所有文件名
    fileNameList = os.listdir(targetPath)
    for fileName in fileNameList:
#        拼接目录
        absPath = os.path.join(targetPath,fileName)
        if  os.path.isdir(absPath): # 判断是否是一个目录
            print("目录名是:%s"%fileName)
            getAllDirAndFile(absPath)
        if  os.path.isfile(absPath):
            print("文件名是:%s"%fileName)

# 测试下
path = r"I:\bj1707"
getAllDirAndFile(path)















