import  pymysql

# 连接数据库
connect = pymysql.Connect(host="localhost",user="root",passwd = "root",database = "wen")
# 获取cursor
cursor = connect.cursor()
# 创建表的sql语句
# sql1 = "drop money if exists"
#如果该表存在,则删除该表
cursor.execute("drop table if exists money")
# 创建该表
cursor.execute("create table money(id int auto_increment primary key,number int not null)")

# 关闭连接
cursor.close()
connect.close()


