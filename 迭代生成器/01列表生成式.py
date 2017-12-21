# 列表生成式
# [1,2,3,4,5]
# for
# print(range(1,101))
# resList = list(range(1,101))
# print(resList)
# print(type(resList)

# 简单的列表生成式
list1 = [i for i in range(1,101)]
# list1 = [i for i in range(1,1000)]
print(list1)
print(type(list1))

#原理
# listNew = []
# for i in range(1,101):
#     listNew.append(i)

# 需求:  生成一个列表    [0,1,4,9,16...]     x^2
# listNew = []
# for i in range(0,101):
#     listNew.append(i*i)

list2 = [i*i for i in range(0,101)]
print(list2)

# 例;  http://bbs.tianya.cn/m/post-140-393974-6.shtml   1-50
list3 = ["http://bbs.tianya.cn/m/post-140-393974-"+str(i)+".shtml" for i in  range(1,51)]
print(list3)

# 需求: [0,2,4,6,8,10,....]  只有偶数的列表
# 需求:  20  <     < 40
# range(0,101,2)

# listNew = []
# for i in range(0,101):
#     if i%2 == 0: #偶数
#         listNew.append(i)

# 在列表生成式中加上 if 条件
# list4 = [i for i in range(0,101) if i%2 == 0]
list4 = [i for i in range(0,101) if i%2 == 0 and i >20 and i < 40]
print(list4)

# 需求:把以下字符串全部转换成小写
list5 = ["Wen","GOOD","18","None","HEllo"]
# lower
# for
# map(lower,list5)
# for i in list5:
#     i.lower()
list6 = [i.lower() for i in list5]
print(list6)

list7 = ["Wen","GOOD",18,None,"HEllo"]
# for i in list7:
#     if isinstance(i,str): #判断i是否是str类型
#         i.lower()

list8 = [i.lower() for i in list7 if isinstance(i,str)]
print(list8)

# 需求: ["x","y","z"] ,["a","b","c"] --->  "xa","xb","xc","ya".......
list9 = ["x","y","z"]
list10 = ["a","b","c"]
# listNew = []
# for i in list9:
#     for j in list10:
#         listNew.append(i + j)

# 列表生成式中可以嵌套for循环
list11 = [i+j for i in list9  for j in list10]
print(list11)







































