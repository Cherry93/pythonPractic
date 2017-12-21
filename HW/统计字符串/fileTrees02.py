import os
from os.path import join,getsize
#没有使用os.walk函数
def walkFolders(folder):
    folderscount=0
    filescount=0
    size=0
    folders=os.listdir(folder) #os.listdir(dirname)：列出dirname下的目录和文件
    for item in folders:
        path=os.path.join(folder,item) #os.path.join(path,name):连接目录与文件名或目录
        if os.path.isdir(path): #os.path.isdir(name):判断name是不是一个目录，name不是目录就返回false
            folderscount+=walkFolders(path)[0]+1
            filescount+=walkFolders(path)[1]
            size+=walkFolders(path)[2]
        elif os.path.isfile(path): #os.path.isfile(name):判断name是不是一个文件，不存在name也返回false
            filescount+=1
            size+=getsize(path) #os.path.getsize(filename):获取filename的文件大小, 单位为字节
    return folderscount,filescount,size
if __name__ == '__main__':
    folder=os.getcwd() #os.getcwd()：获得当前工作目录
    folderscount,filescount,size=walkFolders(folder)
    print (folder,folderscount,filescount,size)