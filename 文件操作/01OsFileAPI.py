'''
os模块提供的文件操作API
'''
import os

import shutil

path = "fuck"#默认路径时当前目录
# path = "./shit" #.=当前目录
# path = "../damn"#..=上一级目录
# path = "C:/Users/idea/Desktop/fuck"#路径分隔符推荐使用"/"，一来兼容Linux，二来免受转义字符之苦
# path = r"C:\Users\idea\Desktop\fuck"#r=该路径中不含转义字符
# path = "C:\\Users\\idea\\Desktop\\fuck"#\\=使用转义字符来表示“\”

# os.mkdir(path)
# os.makedirs("./fuck/shit")
# os.remove("./fuck/fuck.txt")
# os.rmdir("./fuck/shit")
# os.removedirs("./fuck/shit/damn")
# print(os.listdir("../../../"))
# print(os.path.isfile("./fuck"))
# print(os.path.isdir("./fuck"))
# print(os.path.exists("./shit"))

# os.rmdir("./fuck")
# shutil.rmtree("./fuck")