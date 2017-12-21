'''

2. 使用基于UDP(TCP)的Python Socket编程，完成在线咨询功能：

1)   客户向咨询人员咨询。

2)   咨询人员给出回答。

3)   客户和咨询人员可以一直沟通，直到客户发送bye给咨询人员。
'''
import socket
# 创建客户端的socket
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接服务器
clientSocket.connect(("127.0.10.1",22222))

while True:
    # 向服务端发送数据
    sendData = input("客户端说:")
    clientSocket.send(sendData.encode("utf-8"))
    recvData = clientSocket.recv(1024)
    print("服务器说:%s"%(recvData.decode("utf-8")))