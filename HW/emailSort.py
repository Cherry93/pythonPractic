import os
list = []
file = input("Enter a filename:")
with open(file, 'r') as fpr:
    content = fpr.read()
    content = content.split("\n")
    #print(content)
#    content[0].index("@")
    list.append(content[0])
    for i in range(1,len(content)-1):
        #list.append(content[0])
        #print(content[i-1])
    # if "163" in content[0]:
    #     print(content[0])
        str = content[i-1]
        num1 = content[i-1].index("@")
        num2 = content[i-1].index(".")
        #print(num1,num2)
        str1 = str[num1:num2]
        #print( str1)

        if str1 not in content[i]:
          list.append(content[i])
        else:
            pass
#print(list)
# len(list)
        #for i in range(len(list)):
#          if str1 in list[i]:
#             #path1 = os.mkdir(r'E:/%s/'%list[i])
#             # os.mkdir(r"E:/path1/%s.txt"%list[i])
#             #file = path1 + "/" + list[i]
#             with open("2.txt", 'w') as fpw:
#               fpw.write(content[i-1])
#
# print(list)


# emailList = []
# for f in content:
#     if f.endswith() == ""
#
print(list)
# print(len(list))
list2 =[]
for i in range(1,len(content)-1):
        str = content[i-1]
        num1 = content[i-1].index("@")
        num2 = content[i-1].index(".")
        str1 = str[num1:num2]
        list2.append(str1)
#print(list2)
        #print(str1)
        #print(list[0])
        for j in range(len(list)):
            for k in range(len(list2)):
               if list[j].find(str1) != -1:
         #print((r"---------------------E:/files/%s'+'.txt" % list[0]))
                  print(content[i-1])
         # os.mkdir(r'E:/%s/'%list[0])
         # path = "E:/%s/'%list[0]" + "/" + "1.txt"

                  with open("2.txt", 'a') as fpw:
                   fpw.write(content[i-1])

