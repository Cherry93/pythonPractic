# 模拟一个队列数据结构

import collections
# 有双向列表, 有序的set


# 双向列表

# 创建一个双向列表
queue1 = collections.deque()
# 添加数据,默认将数据添加在数据的右端
queue1.append("A")
print(queue1)

queue1.append("B")
print(queue1)

# 表示添加数据,将数据放在数据的左端
# queue1.appendleft("C")
# print(queue1)
queue1.append("C")
queue1.append("D")

#     A  B  C

# 模拟队列取数据,从数据的左端开始取
print(queue1)
data1 = queue1.popleft()
print(data1)
print(queue1)

data2 = queue1.popleft()
print(data2)
print(queue1)
























