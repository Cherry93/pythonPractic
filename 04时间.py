'''
UTC协调时间:  格林威治天文时间,世界标准时间,    UTC+8(北京时间) 中国处于东8区,比世界标准时间快 8个小时
DST 夏令时, 人们为了节约资源而人为的规定的时间,  夏天快一个小时

# 时间的表示形式

1.时间戳
 是一个以整数或者浮点数表示的时间间隔,  从 1970年1月1日, 0分0秒开始计算
  数值

2.时间元组, 有9个元素
年    tm_year  1
月    tm_mon   1-12
日    tm_mday  1-31

时           0-23
分           0-59
秒           0-59

一周中的第几天   0-6(0是周一)
一年中的第几天    1-366
是否是夏令时    0 表示不是   1表示是   -1自己去处理

3.时间字符串
2017 / 02/12   2017-12-12   2017年12月20日  12时12分12秒

%a  本地（locale）简化星期名称
%A  本地完整星期名称
%b  本地简化月份名称
%B  本地完整月份名称
%c  本地相应的日期和时间表示
%d  一个月中的第几天（01 - 31）
%H  一天中的第几个小时（24小时制，00 - 23）
%I  第几个小时（12小时制，01 - 12）
%j  一年中的第几天（001 - 366）
%m  月份（01 - 12）
%M  分钟数（00 - 59）
%p  本地am或者pm的相应符
%S  秒（01 - 61）
%U  一年中的星期数。（00 - 53星期天是一个星期的开始。）第一个星期天之前的所有天数都放在第0周
%w  一个星期中的第几天（0 - 6，0是星期天）
%W  和%U基本相同，不同的是%W以星期一为一个星期的开始。
%x  本地相应日期
%X  本地相应时间
%y  去掉世纪的年份（00 - 99）
%Y  完整的年份
%Z  时区的名字（如果不存在为空字符）
%%  ‘%’字符
'''

import time
# 获取当前的时间戳,是以秒为单位
currentTime = time.time()
print(currentTime)

# 将时间戳转换成时间元组
# gmtime是获取的时间标准UTC时间,当 gmtime没有传递时间戳时,表示获取当前的时间
# tupleTime1 = time.gmtime(currentTime)
# 计算前一天的时间
# tupleTime1 = time.gmtime(currentTime  - 60*60*24)
tupleTime1 = time.gmtime()
print(tupleTime1)

# localtime是获取本地时间, 当localtime没有传递参数时,表示获取当前的本地时间
# tupleTime2 = time.localtime()
tupleTime2 = time.localtime(currentTime)
print(tupleTime2)

# 将时间元组转换成时间戳, 会自动的舍弃小数部分
time2 =  time.mktime(tupleTime2)
print(time2)


# 将时间元组转换成 时间字符串
# 例: 2017-12-13 10:18:00
strTime = time.strftime("%Y-%m-%d %H:%M:%S",tupleTime2)
# strTime = time.strftime("%x %X",tupleTime2)
# 例: 2017年12月13日 10时18分00秒
# strTime = time.strftime("%Y年%m月%d日 %H:%M:%S",tupleTime2)

# 参数1是时间格式
# 参数2是时间元组
# strTime = time.strftime("%Y{y}%m{m}%d{d} %H:%M:%S",tupleTime2).format(y="年",m="月",d="日")
# print(strTime)

# 将时间字符串转换成时间元组
# 参数1是字符串形式的时间
# 参数2是 时间格式, 该格式一定要与字符串时间格式匹配
tupleTime3 = time.strptime(strTime,"%Y-%m-%d %H:%M:%S")
print(tupleTime3)

#让程序睡一会
# print("开始睡")
# # 让程序跑慢点,老板给钱之后再优化
# time.sleep(2)
# print("结束睡")

#在window系统中,用来计算cpu的运行时间,第一次执行时,时间为0.0,后面clock获取的是差值
res = time.clock()
print(res)
time.sleep(2)
res2 = time.clock()
print(res2)
time.sleep(2)
res3 = time.clock()
print(res3)



# 性能测试
# 1+1000000 时间差值, 用time 或者 clock






