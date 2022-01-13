import sqlite3
conn = sqlite3.connect("d:/sql/library1.db")
sqlstr = "create table user (sid varchar(30) primary key, name varchar(30), time varchar(30),jiage varchar(30),kucun varchar(30))"

cur = conn.cursor()
sqlstr1 = "insert into user(sid, name, time,jiage,kucun) values(9787517042099, 'Photoshop入门到创意', '2016-04-01',45.00,5) "
cur.execute(sqlstr1)
sqlstr2 = "insert into user(sid, name, time,jiage,kucun) values(9787115480354, 'SSM轻量级框架应用实战', '2018-05-01',66.80,4) "
cur.execute(sqlstr2)
sqlstr3 = "insert into user(sid, name, time,jiage,kucun) values(9787517042242, 'HTML5+CSS3前端技术', '2016-04-01',52.00,7) "
cur.execute(sqlstr3)
conn.commit()

conn.close()



