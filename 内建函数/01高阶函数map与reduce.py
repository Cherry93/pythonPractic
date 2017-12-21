
'''
高阶函数map,是内置函数
格式:  map(func,data)
func func是一个函数名, 该函数必须至少传入一个参数,该函数必须有返回值
data  是需要处理的数据集合list
返回值是以Iterator,可以转换成list

map函数的作用: 将传入的函数依次作用在序列中的每一个元素,并把结果作为新的Iterator返回
'''

# 需求: ["5","1","3","7","9"] ---- > [5,1,3,7,9]

#  for 循环

# "5"  --->5
def strToInt(strNumber):
    # int(strNumber)
    return  {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}[strNumber]
listData = ["5","1","3","7","9"]
res = map(strToInt,listData)
resList = list(res)
print(resList)
print(type(resList))

# map原理
# def myMap(func,datas):
#     allRes = []
#     for  data in datas:
#         res = func(data)
#         allRes.append(res)
#     return  allRes

# 案例:[5,1,3,7,9]   --->  ["5","1","3","7","9"]
res2 =  map(str,[5,1,3,7,9] )
print(list(res2))


'''
reduce 函数,需要导入 from functools import reduce
格式: reduce(func,datas)
func 表示函数名,需要传递2个参数,return返回两个参数的关系
datas  是需要处理的数据集合list

作用:一个函数作用在序列上,这个函数必须接收2个参数,reduce把结果继续和序列的下一个元素累计运算
1 + 2 + 3 + 4 + 5 +6.......100
原理:  fn(fn(fn(a,b),c),d)....
需求: 实现  1 + 2     + 3 + 4 + 5 +6.......100  的和
# 实现: for循环 ,
# 递归: sum(n) + sum(n-1) ,  找到出口
# reduce实现:
# 只需要考虑 1 + 2
'''
from functools import reduce

def add(a,b):
    return a + b

res = reduce(add,range(1,101))
print(res)
print(type(res))

#需求: "56436789" ---> 56436789   不能使用int

# "56436789" ----> "5","6","4","3" ....map--> 5,6,4,3.....--->56436789
# map  reduce
# int("56436789")

def myInt(strNumber):
    listNumber = list(strNumber)
#   "5" --- >  5
    def strToInt(strNumber):
        # int(strNumber)
        return {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}[strNumber]
    # 5,6 --- > 56
    # 5*10 + 6
    def number(a,b):
        return a*10 + b
    return  reduce(number,map(strToInt,listNumber))

# 测试:
res  = myInt("56436789")
print(res)
print(type(res))





































