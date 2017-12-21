

# 判断一个字符串是否是一个手机号
def isPhoneNumber(number):
    # 13128892388
#   长度是 11位
    if not (len(number) == 11):
        return  False
#   判断第一位必须是 1
    if not (number[0] == "1"):
        return False
#   第二位 可能是 3, 4,5, 7,8
    num = number[1]
    if not (num == "3" or num == "4" or num == "5" or num == "7" or num == "8"):
        return  False
#   13128892388    从第三位到最后一位   范围都是 0-9
    for i in  number[2:]:
        if  not (i >= "0" and i <= "9" ):
            return False
#   证明是合法的手机号码
    return  True

# 验证
print(isPhoneNumber("13128892388"))
print(isPhoneNumber("1312889238"))
print(isPhoneNumber("131288923888"))
print(isPhoneNumber("31288923888"))
print(isPhoneNumber("12889238888"))
print(isPhoneNumber("13u89238888"))



'''
匹配手机号:
phonePattern = "1[34578]\d{9}"

# 匹配qq号码, qq号码是 5-12位的数字
QQPattern = "[1-9]\d{4,11}"

#匹配邮箱地址   xxxxx@xxx.xx
mailPattern = "\w+@\w+\.\w+"

# 匹配是否是163邮箱
mail163Pattern = "\w+@163\.com"
# 末尾可能是 cn 也可能是  com
cn  或者 com
mail163Pattern = "\w+@163\.((com)|(cn))"

匹配一个时间格式:   1980-12-12    01-31
1912-01-01 ------  200
calendarPattern = "((1[89]\d{2})|(20[012]\d))-((0[1-9])|(1[012]))-((0[1-9])|([12][0-9])|(3[01]))"
'''




















