import urllib.request

# 模拟很多个url都需要请求

for i in range(100):
    try:
        responseBaidu = urllib.request.urlopen("https://www.baidu.com/",timeout=3)
        print(responseBaidu.read().decode("utf-8"))
    except :
        print("当url请求出错时,直接将该异常抛掉,然后执行下一次请求")






