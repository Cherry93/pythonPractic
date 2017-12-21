import urllib.request

# urlretrieve可以直接将网页写入到文件中去
# 参数1:用来指定url地址
# 参数2:   fileName直接指定保存的文件路径
urllib.request.urlretrieve("http://www.sina.com.cn/","html/sina.html")
# urllib.request.urlretrieve("http://www.sina.com.cn/",filename="html/sina.html")
# 清理缓存
urllib.request.urlcleanup()












