# 模拟飞秋发送消息
import socket
# 创建udpsocket
# 注意: tcp是以流的形式传输,  udp是以包的形式传输
udpsocket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# 飞秋的端口号是2425
# address = ("10.36.131.81",2425)
#
# str = "1_lbt4_10#32499#002481627512#0#0#0:1289671407:凤姐 :(宝贝):288:我喜欢你很久了,我们在一起吧"
# # 发消息
# udpsocket.sendto(str.encode("gbk"),address)

# 群发
for i in  range(1,255):
    address = ("10.36.131.%d"%(i),2425)
    strData = "1_lbt4_10#32499#002481627512#0#0#0:1289671407:凤姐 :(宝贝):288:班长让我转告大家,今晚吃鸡"
    udpsocket.sendto(strData.encode("gbk"),address)












