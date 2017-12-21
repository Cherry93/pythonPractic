# 导入模块
import  pymysql

# 连接mysql数据库,并得到数据的连接
# host = 主机名
# user = 用户名
# passwd = 密码
# database = 数据库名
# port =  3306 端口号

# connect = pymysql.Connect(host="10.36.131.30",user="root",passwd = "root",database="wen")
# connect = pymysql.Connect(host="127.0.0.1",user="root",passwd = "root",database="wen")
connect = pymysql.Connect(host="localhost",user="root",passwd = "root",database="wen")

# 获取cursor游标对象,可以用cursor游标来操作数据库
cursor = connect.cursor()
# 执行sql语句
sqlStr = "select version()"
cursor.execute(sqlStr)
# 处理执行后的结果
result = cursor.fetchone()
print(result)


# 关闭,释放资源
cursor.close()
connect.close()





