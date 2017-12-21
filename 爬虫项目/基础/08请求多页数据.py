import urllib.request


#定义一个函数用来请求一页数据
def getData(pathUrl):
    response = urllib.request.urlopen(pathUrl)
    strData = response.read().decode("utf-8")
    return strData

if __name__ == '__main__':
    for i in range(1,101):
        pathUrl = "http://litchiapi.jstv.com/api/GetFeeds?column=0&PageSize=20&pageIndex="+str(i)+"&val=100511D3BE5301280E0992C73A9DEC41"
        strdata = getData(pathUrl)
        print(strdata)








