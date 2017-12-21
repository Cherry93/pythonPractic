'''
文件指针
'''

file = open("./doc/4.txt","r+",encoding="utf-8")
print("0",file.tell())
print(file.read())
print("1",file.tell())

file.write("\n")
print("2",file.tell())#\n占了2个文件指针位置

file.write("哈")
print("3",file.tell())#汉字占据3个文件指针位置

file.write("a")
print("4",file.tell())#英文字符占据1个文件指针位置

file.write(".")
print("5",file.tell())#英文字符占据1个文件指针位置

file.write("。")
print("6",file.tell())#英文字符占据1个文件指针位置

file.close()