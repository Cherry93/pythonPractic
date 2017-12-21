import urllib.request
import random
# 模拟一个浏览器头
# headers = {
#     "Accept" : "application/json, text/javascript, */*; q=0.01",
#     "X-Requested-With" : "XMLHttpRequest",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
#     "Content-Type" : "application/x-www-form-urlencoded; charset=UTF-8"
# }
#
# # 将头信息添加到请求体里
# request = urllib.request.Request("https://www.baidu.com/",headers=headers)
# # 用封装好的request发起请求
# responseBaidu = urllib.request.urlopen(request)
# print(responseBaidu.read().decode("utf-8"))


# 创建多个浏览器版本信息,每次访问时随机取一个

agentsList = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"
]

# 随机抽取一个版本信息
userAgent = random.choice(agentsList)
# 创建一个请求体
requestBaidu = urllib.request.Request("https://www.baidu.com/")
# 向请求体中添加useragent
requestBaidu.add_header("User-Agent",userAgent)

# 请求
responseBaidu = urllib.request.urlopen(requestBaidu)
print(responseBaidu.read().decode("utf-8"))






