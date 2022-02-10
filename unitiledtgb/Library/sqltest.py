import sqlite3

conn = sqlite3.connect("d:/sql/library1.db")
print('sql打开成功')
sqlstr = "create table user (sid varchar(30) primary key, name varchar(30), time varchar(30),jiage varchar(30),kucun varchar(30))"
print('表创建成功')