import sqlite3
conn = sqlite3.connect("d:/sql/library.db")
cur = conn.cursor()
sql_delete='delete from user where sid=1'
cur.execute(sql_delete)
conn.commit()


conn.close()
