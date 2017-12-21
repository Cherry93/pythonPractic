import pymysql

connect = pymysql.connect(host="localhost",user="root",passwd="root",database="wen")
cursor = connect.cursor()

try:
    # 插入的sql语句
    insertSql = "insert into money values(0,200),(0,300),(0,400),(0,100),(0,250),(0,350),(0,800),(0,30),(0,200),(0,30)"
    cursor.execute(insertSql)
    # 事务提交,保证数据的完整性,准确性
    connect.commit()
except:
    # 回滚数据,当执行的sql语句中,发生错误时,回滚到执行sql语句之前的状态
    connect.rollback()
cursor.close()
connect.close()








