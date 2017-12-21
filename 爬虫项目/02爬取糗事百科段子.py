import urllib.request
import random
import  re


# 爬取糗事百科段子
def crawlerJoke(urlPath):
#   urllib先爬取网页数据
#   编写正则表达式找出 段子 和 用户名所在整体范围
#   再从整体范围中 找出 段子
#   再从整体范围中 找出 用户名
#   用字典去存储数据

#     urllib.request.urlopen(urlPath)
#   模拟浏览器的头信息
    agentsList = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"
    ]
    userAgent = random.choice(agentsList)
#   封装request
    requestQS = urllib.request.Request(urlPath)
    requestQS.add_header("User-Agent",userAgent)
#   发起请求
    responseQS = urllib.request.urlopen(requestQS)
#   获取网页字符串
    htmlData = responseQS.read().decode("utf-8")

#   读数据数据,写到文件中去
#     with open("qsbk.html","wb") as wf:
#         wf.write(responseQS.read())
#         wf.flush()
#    匹配整体范围的正则表达式
    strPattern = re.compile('<div class="author clearfix">(.*?)<span class="stats-vote"><i class="number">',re.S)
    strList = strPattern.findall(htmlData)
    # 找出段子的正则表达式
    duanziPattern = re.compile('<span>(.*?)</span>',re.S)
    usernamePattern = re.compile('<h2>(.*?)</h2>',re.S)

    # 创建一个空字典用来存储数据 key(用户名)-value(段子)
    dictData = {}

    for strdata in  strList:
#         找出段子
        duanzi = duanziPattern.findall(strdata)[0].strip()
#       找出用户名
        username = usernamePattern.findall(strdata)[0].strip()
        # print(duanzi)
        # print(username)
        dictData[username] = duanzi
    return dictData

def main():
    # urlPath = "https://www.qiushibaike.com/text/page/2/"
    # crawlerJoke(urlPath)

    # 创建一个大的字典存放所有的段子数据
    allDuanzi = {}
    for i in  range(1,14):
        urlPath = "https://www.qiushibaike.com/text/page/"+str(i)
        dictData = crawlerJoke(urlPath)
        allDuanzi.update(dictData)
    # for key in allDuanzi:
    # for key in allDuanzi.keys():
    # for key in allDuanzi.values():
    # for key,value in allDuanzi.items():
    # for index,key in enumerate(allDuanzi):
    print(len(allDuanzi))
    for key,value in allDuanzi.items():
        print("%s说:---%s"%(key,value))





if __name__ == '__main__':
    main()










