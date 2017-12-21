
# with open("1.txt", 'r') as fpr:
#     content = fpr.read()
#     print(content)
import pickle
import os
file = open("11.txt", "r+", encoding="utf-8")
done =0
list1 = []
# for line in file.readlines():
#     print(line)
#一行一行读取文件

# path ="./"+str+"/"+str +".txt"
# file1 = open(path,mode="ab")
while 1:
    line = file.readline()
    if not line:
        break
    pass

    def getstring():
        num1 = line.index("@")
        num2 = line.index(".")
        str = line[num1:num2]
        #print(str)
        path1 = "./"+str
 #       os.mkdir(path1)
        path = path1 + "/" + str + ".txt"
        if not os.path.exists(path1) :
            os.mkdir(path1)
        file1 = open(path, mode="ab")
        pickle.dump(line, file1)
#        return str
    getstring()
# #file.close()
#创建文件夹,返回一个path
    # def creatDir():
    #     path1 = "./"+str
    #     os.mkdir(path1)
    #     return path1





