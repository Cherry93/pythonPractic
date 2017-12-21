from collections  import  Iterable
from collections  import  Iterator


#判断是否是  可迭代对象 Iterable
print(isinstance([],Iterable))
print(isinstance((1,),Iterable))
print(isinstance({},Iterable))
print(isinstance({1,},Iterable))
print(isinstance("",Iterable))

# 判断genertor是否是可迭代对象
genertor1 = (i for i in range(5))
print(isinstance(genertor1,Iterable))

print("------------------------------")
# 判断是否是  迭代器  Iterator
print(isinstance([],Iterator))
print(isinstance((1,),Iterator))
print(isinstance({},Iterator))
print(isinstance({1,},Iterator))
print(isinstance("",Iterator))

#生成器是迭代器,也是可迭代对象
print(isinstance(genertor1,Iterator))

# 将可迭代对象转换成迭代器
list1 = [i for i in range(1,100)]
# 将列表转换成迭代器
itertor1 = iter(list1)
print(itertor1)
print(type(itertor1))

print(next(itertor1))
print(next(itertor1))


# 将元组转换成迭代器
#  iter(元组/列表/字典/)












