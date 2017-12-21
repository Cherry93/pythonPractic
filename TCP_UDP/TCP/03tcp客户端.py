import socket
# 创建客户端的socket
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 连接服务器
clientSocket.connect(("10.36.131.40",22222))

while True:
    # 向服务端发送数据
    sendData = input("客户端说:")
    clientSocket.send(sendData.encode("utf-8"))
    recvData = clientSocket.recv(1024)
    print("服务器说:%s"%(recvData.decode("utf-8")))














