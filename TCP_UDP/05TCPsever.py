import socket
severSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
severSocket.bind(("127.0.0.1",22222))
severSocket.listen(5)
print("waiting connect...")

#接受数据
while True:
    clintServer, address = severSocket.accept()
    try:
        clintServer.settimeout(5)
        clintData = clintServer.recv(1024)

        if clintData =="1":
            clintServer.send("hello,clint...".encode("utf-8"))
        else:
            clintServer.send("please,go out...".encode("utf-8"))
    except severSocket.timeout:
            print("Socket time out...")
            # print("客户端说:%s"%clintData.decode("utf-8"))
            # severData = input("请输入要发送的内容:")
            # clintServer.send(severData.encode("utf-8"))
    finally:
        clintServer.close()

