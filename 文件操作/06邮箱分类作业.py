import os

# 遍历目录 --- 深度遍历
def getAllDirFile(sourcePath):
#     创建一个空的列表
    listPath = []
    listPath.append(sourcePath)
    while True:
        if len(listPath) == 0:
            break
        path = listPath.pop()
        fileNameList = os.listdir(path)
        for fileName in fileNameList:
            absPath = os.path.join(path,fileName)
            if os.path.isdir(absPath):#是否是目录
            #     添加到栈中继续遍历
                listPath.append(absPath)
                # print("目录:",fileName)
            if os.path.isfile(absPath): #是否是文件
                # pass
                # print("文件:",fileName)
                parseData(absPath)

# 用来解析文件
def parseData(filePath):
    targetPath = r"C:\Users\wenyucheng\Desktop\资料\作业\res"
#     打开一个文件
    with open(filePath,"r",encoding="utf-8",errors="ignore") as rf:
#         一行一行的读取文件
        while True:
            lineData = rf.readline()
            if len(lineData) == 0: #读完了
                break
#            一行数据 :  xiaozhuc-o-o-l@163.com----henry19891010
#            将账号和秘密分割
            userStr = lineData.split("----")[0]
            # 找到 "@" 的位置
#             indexA = userStr.rfind("@")
# #           找到 .的位置
#             indexD =  userStr.rfind(".")
# #           截取类型
#             mailType = userStr[indexA+1:indexD]
#             print(mailType)

# 另外一种方式
#               xiaozhuc-o-o-l@163.com.cn
#           获取到邮箱类型
            mailType =  userStr.split("@")[1].split(".")[0]
            # print(mailType)

#            拼接目录
            typeDir = os.path.join(targetPath,mailType)
#           判断该类型对应的目录是否存在
            if not os.path.exists(typeDir): #如果该目录不存在则创建该目录
                # mkdir
                os.makedirs(typeDir)

#            拼接文件路径
            typeFilePath = os.path.join(typeDir, mailType + ".txt")
#           将邮箱追加到文件中去
            with open(typeFilePath,"a",encoding="utf-8") as af:
                af.write(userStr + "\n")
                af.flush()
def main():
    # pass
    sourcePath = r"C:\Users\wenyucheng\Desktop\资料\作业\newdir"
    getAllDirFile(sourcePath)


if __name__ == '__main__':
    main()



