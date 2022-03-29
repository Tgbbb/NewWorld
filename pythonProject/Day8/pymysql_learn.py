import pymysql

connect = pymysql.connect(host='localhost',
                          user='root',
                          password='540aa539',
                          database='test',
                          port=3306,
                          charset='utf8mb4',
                          cursorclass=pymysql.cursors.DictCursor)
cursor = connect.cursor()
# sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
# cursor.execute(sql, ('843682137@qq.com', '123456'))
#
# connect.commit() # 增删改需要commit

sql = "select * from users"
cursor.execute(sql)
result = cursor.fetchall()  # fetchone只保留一条数据(类型为字典).类似方法还是fetchmany（填数据数），fetchall（查询所有），这两个都有多条数据，类型就是数组
print(type(result))
print(result)
