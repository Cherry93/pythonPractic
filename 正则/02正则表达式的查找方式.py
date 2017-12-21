# 导入正则表达式的的模块 re
import re
#  查找方式
'''
re.match()    表示从字符串的开始位置开始匹配正则条件的字符
re.search()   找出字符串中第一个符合正则条件的字符
re.findall()  找出字符串中所有符合正则条件的字符
'''
'''
re.match(pattern,string,flags)
pattern  正则表达式
string  代表是源字符串
flags   标记
    re.I   表示匹配对大小写不敏感
    re.M   多行匹配时是否影响 ^ 和 $
    re.S   使 . 匹配包括换行在内的所有字符

'''
# 如果匹配成功会返回一个匹配对象
# 如果匹配不成功,则返回None
# res = re.match("www","www.baidu.com")
# res = re.match("www","awww.baidu.com")
# res = re.match("www","awww.baiwwwdu.com")
# res = re.match("www","wwwww.baidu.com")
# res = re.match("www","WWW.baidu.com")
# re.I表示忽略大消息
# res = re.match("www","WWW.baidu.com",re.I)
# print(res)

#
'''
re.search()   找出字符串中第一个符合正则条件的字符
pattern 表示正则表达式
string 查找的源字符串
flags 表示查找的标记, 可以省略

'''
# res = re.search("www","www.baidu.com")
# res = re.search("www","awww.baidu.com")
# res = re.search("www","awwwww.baidu.com")
# res = re.search("www","awww.baiduwww.com")
# span方法表示获取找到的结果在源字符串中的位置
# res = re.search("www","awww.baiduwww.com").span()
res = re.search("www","aWww.baiduwww.com",re.I)
print(res)

'''
re.findall()  找出字符串中所有符合正则条件的字符
'''
# 匹配的结果是一个列表, 列表中的元素是匹配成功的字符串
# 注意:如果一个都没有匹配上, 则返回一个空的列表
# res = re.findall("www","www.baidu.com")
# res = re.findall("www","ww.baidu.com")
# res = re.findall("www","www.baiWwwdu.com")
# res = re.findall("www","www.baiWwwdu.com",re.I)
res = re.findall("www","wwwww.baiWwwdu.com",re.I)
print(res)
print(type(res))





