# udp的客户端
import socket
udpClientSocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
#    发送消息给服务器
    sendData = input("客户端说:")
    udpClientSocket.sendto(sendData.encode("utf-8"),("10.36.131.40",33333))

#   接收服务器的数据
    recvData,address = udpClientSocket.recvfrom(1024)
    print("服务器说:%s"%(recvData.decode("utf-8")))









