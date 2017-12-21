# 导入urllib库
import urllib.request

# 使用request进行网络请求,直接传入网址就行了
# 会返回响应体
responseBaidu = urllib.request.urlopen("http://www.baidu.com/")
# print(response)
# print(type(response))
# 获取数据
# 获取所有的数据
# recvData = responseBaidu.read().decode("utf-8")
# print(recvData)

# 读取一定长度的数据
# recvData = responseBaidu.read(1024).decode("utf-8")


# 获取一行数据
# recvData = responseBaidu.readline().decode("utf-8")
#读取多行
# recvData = responseBaidu.readlines()
# print(recvData[200].decode("utf-8"))
# print(recvData)

# 将数据写到文件中去
# with open("html/baidu.html","wb") as wf:
#     wf.write(responseBaidu.read())
#     wf.flush()

# 获取响应信息
# responseInfo = responseBaidu.info()
# print(responseInfo)

# getcode表示获取响应状态码
# 200表示请求成功, 404 表示没有找到对应资源
# code = responseBaidu.getcode()
# print(code)
#
# if responseBaidu.getcode() == 200:
#     # 表示请求成功
#     pass

# 获取请响应的url
print(responseBaidu.geturl())













