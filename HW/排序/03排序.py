#冒泡排序:从小到大
#选择排序
#插入排序
#[45,23,12,78,34,54,13,33]
def bubble(bubbleList):
  num =len(bubbleList)
  while num >0:
    for i in range(1,num):
        if bubbleList[i-1] >bubbleList[i]:
            #bubbleList.pop(bubbleList[i-1] )
            bubbleList[i-1] = bubbleList[i]+bubbleList[i-1]
            bubbleList[i] = bubbleList[i-1]-bubbleList[i]
            bubbleList[i-1] = bubbleList[i-1]-bubbleList[i]
            #bubbleList[i-1] = bubbleList[i]
    num -= 1
    print(bubbleList)
#bubble([45,23,12,78,34,54,13,33])


#选择排序
def mySelect(selList):
    len1 = len(selList)
    mylist=[]
    while len1 >0:
        for i in range(len(selList)):
            num = max(selList)
            mylist.append(num)
            selList.pop(selList.index(num))

        len1 -=1
    print(mylist)
mySelect([45,23,12,78,34,54,13,33])

#插入排序
'''
谓插入排序法，就是检查第i个数字，如果在它的左边的数字比它大，进行交换，这个动作一直继续下去，直到这个数字的左边数字比它还要小，
就可以停止了。插入排序法主要的回圈有两个变数：i和j，每一次执行这个回圈，就会将第i个数字放到左边恰当的位置去。
'''

def insert(inserList):

    leng = len(inserList)
    print(leng)
    for i in range(1,leng):
        tmp = inserList[i]
        #print(tmp)
        j = i-1
        while j>=0:
            if tmp <inserList[j]:
                # inserList[i] = inserList[j]

                inserList[j+1] = inserList[j]
                #print(inserList[j+1] )
                inserList[j] = tmp
                #print(inserList[j])
                #print(inserList)
            j -=1
    print(inserList)


insert([45,23,12,78,34,54,13,33])









