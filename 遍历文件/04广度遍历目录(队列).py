import os
import collections


def  getAllDirAndFile(targetPath):
    #    创建一个双向列表,用来存放路径
     queuePath = collections.deque()
    #    把第一个路径放进去
     queuePath.append(targetPath)

     while True:
         # 当队列中没有值的时候,终止该遍历
         if len(queuePath) == 0:
            break
        #     把一个路劲取出来
         filepath = queuePath.popleft()
         # print(filepath)

        #     获取到该目录下的所有文件名
         fileNameList = os.listdir(filepath)
         for fileName in fileNameList:
        #        拼接目录
            absPath = os.path.join(filepath,fileName)
            if  os.path.isdir(absPath): # 判断是否是一个目录
                print("目录名是:%s"%fileName)
            #   如果是目录,则将该目录加到队列中去
                queuePath.append(absPath)
            if  os.path.isfile(absPath):
                print("文件名是:%s"%fileName)

# 测试
if __name__ == '__main__':
    path =r"C:\Users\wenyucheng\Desktop\资料\作业\newdir"
    getAllDirAndFile(path)





