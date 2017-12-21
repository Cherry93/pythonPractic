import socket
#创建服务器socket
serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 给该服务绑定ip地址和端口号
serverSocket.bind(("10.36.131.40",22222))
# 设置可以接收的客户端的数量
serverSocket.listen(5)

# accept方法会阻塞程序的运行
print("服务器启动了")
# 等待客户端的接收
clientSocket,address = serverSocket.accept()
# clientSocket是连接服务器的客户端socket对象
# address是客户端的地址(ip,端口)
print(clientSocket)
print(address)
print("接收到了客户端的连接")

while True:
    # 接收客户端的数据
    recvdata = clientSocket.recv(1024)
    print("客户端说:%s"%(recvdata.decode("utf-8")))
    senddata = input("服务器说:")
    # 发送给客户端的消息
    clientSocket.send(senddata.encode("utf-8"))







