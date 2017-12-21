
import urllib.request
import re
page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}
try:
    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    strdata = response.read().decode("utf-8")
    #dzPartern = re.compile("<span>.*?</span>")
    dzPartern = re.compile(u'<div class="content">(.*?)</div>',re.S)
    auPartern = re.compile(u'<h2>(.*?)</h2>',re.S)
    resd = dzPartern.findall(strdata)
    resa = auPartern.findall(strdata)

    if resa:
        for i in range(len(resa)):
            res = str(i)+resa[i].strip() + resd[i].strip()
            print(res)

    # print(strdata)
except :
    print("当url请求出错时,直接将该异常抛掉,然后执行下一次请求")


