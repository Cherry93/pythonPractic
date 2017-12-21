# 排序
# 冒泡
# numbers = [34,26,77,100,1,20,-66,666]
# # 从小到大
# for i in range(len(numbers)-1):#需要比较几轮
#     for j in range(len(numbers)-1-i):  #比几次
#        if  numbers[j]  >  numbers[j+1]:
# #             交换位置
#             numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
# print(numbers)




# 选择
# numbers = [34,26,77,100,1,20,-66,666]
# for i in range(len(numbers)-1): #要取多少次
#     index = i
#     for j in range(i+1,len(numbers)):
#         if numbers[j] < numbers[index]:
#             index = j
#     numbers[i],numbers[index]= numbers[index],numbers[i]
#
# print(numbers)
# 插入

numbers = [34,26,77,100,1,20,-66,666]
for i in range(1,len(numbers)):
    j = i - 1
    if numbers[i] <  numbers[j]:
        temp = numbers[i]
        numbers[i] = numbers[j]

        j = j -1
        while j >= 0 and temp < numbers[j]:
            numbers[j+1] = numbers[j]
            j = j -1
        numbers[j+1] = temp
print(numbers)







