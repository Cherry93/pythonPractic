import re

# 字符串拆分
# strData = "wen is a nice man"
# strData = "wen    is   a    nice    man"
# listData = strData.split()
# listData = strData.split(" ")
# print(listData)

# 正则表达式拆分字符串
# pattern 表示正则表达式, 即以什么字符为分割点进行拆分
# String 表示需要被拆分的元字符
# maxsplit  表示最大拆分的次数
# flags  标记
# listData = re.split(" +",strData)
# print(listData)


# 字符串替换
strData = "wen is very Very Very very good man"
# strData.replace()
# 用正则表达式来替换
'''
pattern
repl  用来替换的新字符串
string  源字符串
count 代表替换的次数,默认是全部替换
flags
'''
# res = re.sub("very","good",strData)
# res = re.sub("very","good",strData,flags=re.I)
# res = re.sub("very","good",strData,1,flags=re.I)

# subn方法与sub方法作用一样,用来替换字符串,
# sub只返回替换后的字符,
# subn返回两个值,  值1: 表示替换后的字符,  值2:表示被替换的次数
res = re.subn("very","good",strData,2,flags=re.I)
print(res)




