from TestFengzhuang.db_config import MysqlDb

db = MysqlDb() # 为MysqlDb这个类实例化一个对象db

sql = "select * from users"

res = db.get_all(sql) # 用一个变量去接收get_one的return值
print(res)

db.close()