import urllib.request
import random
import re
import os

# 爬取亚马逊女装图片
def crawlerImage(urlPath):
    #   模拟浏览器的头信息
    agentsList = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0"
    ]
    userAgent = random.choice(agentsList)
    #   封装request
    requestYMX = urllib.request.Request(urlPath)
    requestYMX.add_header("User-Agent", userAgent)
    #   发起请求
    responseYMX = urllib.request.urlopen(requestYMX)
    #   获取网页字符串
    htmlData = responseYMX.read().decode("utf-8")
#    向文件中写入
#     with open("yamaxun.html","wb") as wf:
#         wf.write(responseYMX.read())
#         wf.flush()
#     超出图片的url地址
#    编写图片地址的正则表达式
    imgPattern1 = re.compile('data-a-image-source="(.*?)">')
    imgPattern2 = re.compile('<img alt="&#20135;&#21697;&#35814;&#32454;&#20449;&#24687;" src="(.*?)"')
#   查找该页所有的图片地址
    listUrl1 = imgPattern1.findall(htmlData)
    listUrl2 = imgPattern2.findall(htmlData)
    # print(listUrl1)
    # print(listUrl2)
    # print(len(listUrl1))
    # print(len(listUrl2))

    listUrl1.extend(listUrl2)
#   下载到文件中去
    for imageUrlPath  in listUrl1:
        # 获取图片的名字

        # 获取路径最后一个 "/" 的位置
        index = imageUrlPath.rfind("/")
        imgFileName = imageUrlPath[index+1:]

        # 图片完整的路径
        absPath = os.path.join(r"C:\Users\wenyucheng\Desktop\资料\images",imgFileName)
        urllib.request.urlretrieve(imageUrlPath,filename=absPath)

def main():
    urlPath = "https://www.amazon.cn/s/ref=nb_sb_noss?__mk_zh_CN=%E4%BA%9A%E9%A9%AC%E9%80%8A%E7%BD%91%E7%AB%99&url=search-alias%3Daps&field-keywords=%E5%A5%B3%E8%A3%85&rh=i%3Aaps%2Ck%3A%E5%A5%B3%E8%A3%85"
    crawlerImage(urlPath)



if __name__ == '__main__':
    main()



