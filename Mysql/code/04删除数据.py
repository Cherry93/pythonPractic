import pymysql

db = pymysql.connect(host="localhost",user="root",passwd="root",database="wen")
cursor = db.cursor()

try:
    # delete 删除数据
    deleteSql = "delete from money where number > 300"
    # 执行
    cursor.execute(deleteSql)
    # 提交
    db.commit()
except:
    # 回滚
    db.rollback()
cursor.close()
db.close()