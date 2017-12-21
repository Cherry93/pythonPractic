import urllib.request
import re
page = 0
list1=[]
for i in range(50):
    page += 1
    url = "http://bbs.tianya.cn/m/post-140-393974-"+str(page)+"."+"shtml"
    response = urllib.request.urlopen(url)
    strData = response.read().decode("utf-8")
    qqPartern = re.compile("[Qq]{2}" ,re.I)
    numPartern = re.compile("[1-9]\\d{4,10}")
    resq = qqPartern.findall(strData)
    resu = numPartern.findall(strData)
    for j in range(len(resq)):
        if resq:
            res = resq[j]+":" + resu[j]
            list1.append(res)
print(list1)