# 排序
# 冒泡,选择,插入

#
dataList = [34,67,12,23,78,54]
# 默认升序
# dataList.sort()
resList = sorted(dataList)
print(resList)

# 降序
resList = sorted(dataList,reverse = True)
print(resList)

# 绝对值的大小排序
dataList = [34,-67,12,23,-78,54]
resList = sorted(dataList,key = abs)
print(resList)

#按字符的长度排序
dataList = ["金三胖胖","安培shanshan","奥巴马","普京大帝","摩的asan"]
# resList = sorted(dataList)
# print(resList)
def getLength(strName):
    return  len(strName)
resList = sorted(dataList,key=getLength)
print(resList)







