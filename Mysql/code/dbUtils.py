import pymysql

class  DBUtils(object):
    def __init__(self,host="localhost",user="root",passwd="root",database = "wen",charset="utf8"):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.database = database
        self.charset = charset
#     连接数据库
    def connect(self):
        self.db = pymysql.connect(self.host,self.user,self.passwd,self.database,self.charset)
        self.cursor = self.db.cursor()

#   关闭数据库
    def close(self):
        self.cursor.close()
        self.db.close()
#   增加,删除,修改,查找一个,查找多个

#   查找一个
    def  getOne(self,sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchone()
        self.close()
        # 将结果封装成 - 对象
        return res
#   作业




