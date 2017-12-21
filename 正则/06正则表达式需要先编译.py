import re

# 匹配手机号:
# phonePattern = "1[34578]\d{9}"
# 如果该正则表达式需要使用多次,最好先编译在使用
# pattern 需要编译的正则字符串
# flags  标记
# 返回一个编译后的正则
phonePattern = re.compile("1[34578]\d{9}")
# 编译后的正则如何使用?
# re.match()
# ---->phonePattern.match()
# re.search()
# ---->phonePattern.search()
# re.findall()
# ---->phonePattern.findall()

# 直接传递需要匹配的源字符,匹配后的结果与  re.match()/search/findall一样
# res = phonePattern.match("13128892388")
res = phonePattern.match("1328892388")
print(res)








