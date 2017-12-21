'''
get请求:
get请求直接将需要传递的参数放在url的后面
优点:速度快,数据直观
缺点: 不安全, 传输的数据量小
如:  http://litchiapi.jstv.com/api/GetFeeds?column=0&PageSize=10&pageIndex=1&val=100511D3BE5301280E0992C73A9DEC41
'''
#
import urllib.request
strPath = "http://litchiapi.jstv.com/api/GetFeeds?column=0&PageSize=30&pageIndex=2&val=100511D3BE5301280E0992C73A9DEC41"
responseNews = urllib.request.urlopen(strPath)
print(responseNews.read().decode("utf-8"))








