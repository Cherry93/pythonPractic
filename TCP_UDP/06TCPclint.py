import socket
import time
clintSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clintSocket.connect(("127.0.0.1",22222))

#接受数据
# while True:
#     senData = input("请输入您要发送的内容:")
#     clintSocket.send(senData.encode("utf-8"))
#     seveDate = clintSocket.recv(1024)
#     print("服务器说:%s"%seveDate.decode("utf-8"))
time.sleep(2)
clintSocket.send("1".encode("utf-8"))
print(clintSocket.recv(1024))
clintSocket.close()