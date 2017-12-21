# udp服务端
import socket
udpServerSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 给服务绑定端口和ip
udpServerSocket.bind(("10.36.131.40",33333))
while True:
    # recvfrom 会接收udp数据,并返回两个值
    # data 代表的是另一端发送的数据
    # address 代表的是另一端的地址
    data,address = udpServerSocket.recvfrom(1024)
    print(address)
    print("客户端说:%s"%(data.decode("utf-8")))
#   回复消息给客户端
    sendData = input("服务器说:")
    udpServerSocket.sendto(sendData.encode("utf-8"),address)





