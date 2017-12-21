# 模拟一个栈,   堆栈

list1 = []

#压栈
list1.append("A")
print(list1)

# 压栈,即往数据集合中添加一个数据,默认是往数据的尾部添加
list1.append("B")

list1.append("C")

list1.append("D")
print(list1)


# 出栈, 即从数据集合中取住数据,最后存进去的最先取出来,就是从数据的尾部取
# 默认删除最后一个值,并将值返回
data1 = list1.pop()
print(data1)
print(list1)

data2 = list1.pop()
print(data2)
print(list1)






















