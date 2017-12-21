# 正则表达式不仅仅有强大的匹配功能,还有强大的字符串提取功能, 就是使用分组提取
import re


number = "010-83798978,010-83798978"
# 正则表达式匹配给座机号
# pattern = "\d{3}-\d{8}"
# pattern = "(\d{3})-(\d{8})"
pattern = "((?P<first>\d{3})-(?P<last>\d{8}))"
# res = re.match(pattern,number)
# print(res)
res = re.findall(pattern,number)
print(res)


# ( ) 会将数据按()的顺序进行分组,
# print(res.group())
# print(res.group(0))
# print(res.group(1))
# print(res.group(2))
# # 多个组组成的元组
# print(res.groups())

# 根据别名来获取数据,   格式:(?P<名称>正则)
# print(res.group("first"))
# print(res.group("last"))

















