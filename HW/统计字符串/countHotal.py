'''

 统计加州旅馆中所有单词出现的次数，并降序打印
'''
import collections
file = input("Enter a filename:")
with open(file, 'r') as fpr:
    content = fpr.read()

content = content.replace("\n", '')
content1 = content.split()
print(content1)
print(content1[0].lower())
print(len(content1))
list =[]
for i in range(0,len(content1)):
    list.append(content1[i].lower())
print(list)
print("\n各单词出现的个数：\n%s"%collections.Counter(list))

#content2 = content1.lower()
#print(content1)

