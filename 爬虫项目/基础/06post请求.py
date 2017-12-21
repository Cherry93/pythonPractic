'''
post请求:
将请求参数封装成一个数据包,单独传输
优点: 安全,可以传输大数据
缺点: 速度就慢,数据不直观
'''
import urllib.request
import urllib.parse
# 用字典封装post请求的参数
postParms = {"pageNo":"1",
              "pageSize":"20",
              "serialIds":"2143,3404",
              "v":"4.0.0"}

# 将字典类型的post请求参数设置到请求体中
parms = urllib.parse.urlencode(postParms).encode("utf-8")
urlPath = "http://mrobot.pcauto.com.cn/v2/cms/channels/1"
request = urllib.request.Request(urlPath,parms)
# 发起请求
response = urllib.request.urlopen(request)
print(response.read().decode("utf-8"))






