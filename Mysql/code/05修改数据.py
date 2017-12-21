import pymysql

# 注意:操作中文时, 需要指定编码
db = pymysql.connect(host="localhost",user="root",passwd="root",database="wen",charset="utf8")
cursor = db.cursor()

try:
    # delete 删除数据
    # deleteSql = "update money set number = 250 where number = 30"
    # deleteSql = 'update student set address = "北京" where address = "深圳"'
    deleteSql = "update student set address = '深圳' where address = '北京'"

    # 执行
    cursor.execute(deleteSql)
    # 提交
    db.commit()
except:
    # 回滚
    db.rollback()
cursor.close()
db.close()