'''
文件遍历
'''

# 使用with结构，实现文件操作完毕自动关闭并释放
with open("./doc/1.txt","r+",encoding="utf-8") as file:

    # 方式1：读入全部内容
    # content = file.read()
    # print(content)

    # 方式2：迭代器式遍历
    # for line in file:
    #     print(line)

    # 方式3：列表式遍历
    for line in file.readlines():
        print(line)

    pass