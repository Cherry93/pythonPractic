'''
filter 过滤器,是内置函数
filter(func,datas)
func 是一个函数名
datas  是一个需要处理的数据集合list

作用: 把传入的函数依次作用于序列每一个元素,根据返回的True还是False决定是否保留该元素
'''
# 需求: 获取0-20之间的奇数
# listData = list(range(21))
# def isOdd(number):
#     if number%2 != 0: #表示时奇数
#         return True
#     return False
# res = filter(isOdd,listData)
# print(res)
# print(type(res))
# print(list(res))

# 需求: 0,1   True,False   "None",""   1,2
listData = [" ","金三胖胖","奥巴马","安培珊珊","None",""]
# 非零即为真,非空即为真

# def isFilter(data):
#     if data==" " or data == "None" or data=="":
#         return False
#     return  True
# res = filter(isFilter,listData)
# print(list(res))

listData = list(range(1,5))
#1,2,3,4
for i in listData:
    if i == 2:
        listData.remove(i)
    print(i)

#  for  i=0;i < 10;i++    0,1,2,3,4,...9
#   0
# 1 ,3,4



















