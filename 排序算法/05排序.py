
'''
冒泡法，两两比较，左边比右边大就换位子
'''


def bubble(mylist):
    num = len(mylist)
    while num>0:
        for i in range(1,num):
            if mylist[i-1]> mylist[i]:
                mylist[i-1],mylist[i] = mylist[i],mylist[i-1]
        num -=1
    print(mylist)

bubble([2,4,7,9,3,5])

'''
选择，先选择出最大或者最小
'''
def select(mylist):
    num = len(mylist)
    for i in range(num):
        index = i
        for j in range(i+1,num):
            if mylist[j]<mylist[index]:
                index=j
                mylist[i],mylist[index] = mylist[index],mylist[i]
    print(mylist)
select([2,4,7,9,3,5])

