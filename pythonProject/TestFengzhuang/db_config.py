import pymysql

class MysqlDb:
    def __init__(self):  # 封装数据库的构造函数，初始方法，一般都是去连接这个数据库
        self.connect = pymysql.connect(host='localhost',
                                  user='root',
                                  password='540aa539',
                                  database='test',
                                  port=3306,
                                  charset='utf8mb4',
                                  cursorclass=pymysql.cursors.DictCursor)

    def get_one(self, sql):
        with self.connect.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchone()
    def get_all(self, sql):
        with self.connect.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchall()
    def get_many(self, sql, sqlnum = None):
        with self.connect.cursor() as cursor:
            cursor.execute(sql)
            return cursor.fetchmany(sqlnum)
    def executeSql(self, sql):
        with self.connect.cursor() as cursor:
            cursor.execute(sql)
            self.connect.commit()

    def close(self):
        self.connect.close()
