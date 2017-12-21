# tcp请求新浪网页
import socket

#创建socket,
# 参数1: socket.AF_INET 表示的是ip协议版本,AF_INET表示的是ipv4,AF_INET6表示的是ipv6
# 参数2: 数据以流的形式传输
socketTCP = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 连接新浪服务器
#"www.sina.com.cn" ---->DNS域名解析服务器--->ip地址
# address参数表示服务器地址, 该参数以元组的方法传输, 元素1表示ip地址,元素2表示端口号
socketTCP.connect(("www.sina.com.cn",80))

# 发送网络请求
socketTCP.send(b"GET / HTTP/1.1\r\nHost:www.sina.com.cn\r\n\r\n")

# 接收数据
dataList = []
# 将网页写到文件中去
# 打开一个文件
# wf = open("sina.html","wb")
while True:
    content = socketTCP.recv(1024)
    if len(content) == 0:  #数据读取完毕
        break
    # 写文件
    # wf.write(content)
    # wf.flush()

    # 把数据加到列表
    dataList.append(content)
# 关闭文件
# wf.close()
dataStr = b"".join(dataList).decode("utf-8")
# print(dataStr)

# 关闭连接
# socketTCP.close()

# 分离响应头和html
head,html = dataStr.split("\r\n\r\n",1)
# print(head)
print(html)














