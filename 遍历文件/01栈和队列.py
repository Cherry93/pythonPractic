'''
栈是先进后出，队列是先进先出，就像排队
实现文件遍历的三种方式：
1，递归遍历
2，深度遍历（栈）
3，广度遍历（队列）

'''

#递归遍历,递归函数，自己调用自己
import os

def findFile(urlPath):
    #首先罗列出路径下所有文件,得到的一个文件名列表
    fileNmaeList = os.listdir(urlPath)
    #遍历该文件名
    for filename in fileNmaeList:
        #文件的绝对路径
        absPath = os.path.join(filename,urlPath)
        #如果是文件夹继续往下找，
        if os.path.isdir(absPath):
            print("目录是：",filename)
            findFile(absPath)
        if os.path.isfile(absPath):
            print("文件是:",filename)
    # return filename

#深度遍历，使用list


