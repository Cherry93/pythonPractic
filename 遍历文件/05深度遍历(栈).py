import os


def  getAllDirAndFile(targetPath):
    pathList = []
#   放第一个目录
    pathList.append(targetPath)

    while True:
        if len(pathList) == 0:
            break
    #   获取栈中的目录
        path = pathList.pop()

    #     获取到该目录下的所有文件名
        fileNameList = os.listdir(path)
        for fileName in fileNameList:
    #        拼接目录
            absPath = os.path.join(path,fileName)
            if  os.path.isdir(absPath): # 判断是否是一个目录
                print("目录名是:%s"%fileName)
                pathList.append(absPath)
            if  os.path.isfile(absPath):
                print("文件名是:%s"%fileName)

# 测试
if __name__ == '__main__':
    path =r"C:\Users\wenyucheng\Desktop\资料\作业\newdir"
    getAllDirAndFile(path)




