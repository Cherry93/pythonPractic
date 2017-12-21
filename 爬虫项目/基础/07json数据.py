'''
json是一种字符串数据格式:
可以存储到文件中去,可以跨平台传输,是轻量级的数据
{} 表示包裹一个对象
[] 可以包含多个对象,也可以包含多个值
key:value   key属性名    value是属性值  中间用 : 连接
,     属性与属性之间用 , 连接
'''

import json
# 创建一个json数据
# jsonData = '{"name":"金三胖胖","age":35,"likes":[{},{},{}]}'
jsonData = '{"name":"金三胖胖","age":35,"likes":["金钱","权利","beautifulgirl"]}'
# 将字符串形式的json转换成字典使用
dictRes = json.loads(jsonData)
# print(dictRes)
# print(type(dictRes))
# print(dictRes["likes"])
# print(dictRes["name"])


# 将字典形式 转换成json形式字符串
strJson =json.dumps(dictRes)
print(strJson)
print(type(strJson))


# 将文件中的json数据读取出来,并转换成字典
with open("city.json","r",encoding="utf-8") as rf:
    dictFileRes = json.load(rf)
    print(dictFileRes)
    print(type(dictFileRes))

#将字典形式的json/字符串形式的json 写到json文件中去
with open("city.txt","w",encoding="utf-8") as wf:
    # 将字典形式的数据写到文件中去
    # json.dump(dictFileRes,wf)
    # 将字符串形式的json写入到文件中去
    json.dump(strJson,wf)


















