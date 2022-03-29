from TestFengzhuang.db_config import MysqlDb

db = MysqlDb()

sql = "select * from users"

res = db.get_one(sql) # 用一个变量去接收get_one的return值
print(res)

db.close()