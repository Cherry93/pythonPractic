
'''

1)   要求从客户端录入几个字符，发送到服务器端。

2)   由服务器端将接收到的字符进行输出。

3)   服务器端向客户端发出“您的信息已收到”作为响应。

4)   客户端接收服务器端的响应信息。
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