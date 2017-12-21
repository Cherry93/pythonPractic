import pymysql

db = pymysql.connect("localhost","root","root","wen",charset="utf8")
cursor = db.cursor()

'''
fetchone是 一行一行的读取结果,
rowcount 属性,是获取结果总共有多少行
fetchall 读取所有的结果
fetchmany 读取指定数量的结果
'''



# 进行查询
selectSQL = "select * from students"
cursor.execute(selectSQL)
# 查询之后的结果,会在cursor中
# 取
# 一条一条的取,结果是元组的形式
# res1 = cursor.fetchone()
# print(res1)
# # print(type(res1))
# res2 = cursor.fetchone()
# print(res2)

# 读取所有的数据
# for i in range(cursor.rowcount):
#    res = cursor.fetchone()
#    print(res)

# 获取所有
# for data in cursor.fetchall():
#     print(data)

for data in cursor.fetchmany(4):
    print(data)




cursor.close()
db.close()



