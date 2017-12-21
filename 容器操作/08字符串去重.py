'''
请实现在一个字符串中查找重复字母的python脚本，并手工演算出前四次循环的结果，写在答案里。

思路：字符串遍历放到列表，再用集合去重
'''

list1 =[]
str1 = "sjeuddjdsad"
for i in str1:
    # print(i)
    list1.append(i)
    res = set(list1)
# print(res)
'''
用无限循环语句显示一系列数字（1、2、3、4、5……），并设置当用户按下某个按钮时（如ESC键）程序就会中止；

'''

'''
让用户输入一些数字或字符串，以升序或降序进行排列
'''
'''
将一个文本文件转换成网页文件（文件输入输出操作、字符串操作）
'''

# 方法1：使用read()和write()模拟实现文件拷贝

# 创建文件hello.txt
src = open("hello.txt", "w")
li = ["Hello world \n", "Hello China \n"]

src.writelines(li)
src.close()

# 把hello.txt 拷贝到hello2.txt

src = open("hello.txt", "r")
dst = open("hello2.txt", "w")

dst.write(src.read())

src.close()
dst.close()

