# import socket
#
# clintSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #链接服务器
# clintSocket.connect(("127.0.0.1",22222))
#
#
# while True:
#     sData = input("客户端说：")
#     clintSocket.send(sData.encode("utf-8"))
#     rData = clintSocket.recv(1024)
#     print("服务器说：",sData.encode("utf-8"))

import socket
import threading

def sock_conn():
    client = socket.socket()
    client.connect(("localhost",8001))
    count = 0
    while True:
        #msg = input(">>:").strip()
        #if len(msg) == 0:continue
        client.send( ("hello %s" %count).encode("utf-8"))
        data = client.recv(1024)
        print("[%s]recv from server:" % threading.get_ident(),data.decode()) #结果
        count +=1
    client.close()

if __name__ == '__main__':

    for i in range(100):
        t = threading.Thread(target=sock_conn)
        t.start()