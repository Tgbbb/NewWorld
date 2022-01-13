from tkinter import *
from tkinter import ttk
import sqlite3
conn = sqlite3.connect("d:/sql/library.db")
cur = conn.cursor()

win=Toplevel()
win.geometry('570x200')
win.title("书目信息")

columns = ("编号", "书名","时间","价格")
treeview=ttk.Treeview(win,height=20,show='headings',columns=columns)

treeview.column("编号", width=200, anchor='center')
treeview.column("书名", width=200, anchor='center')
treeview.column("时间", width=100, anchor='center')
treeview.column("价格", width=70, anchor='center')

treeview.heading("编号", text="编号")  # 显示表头
treeview.heading("书名", text="书名")
treeview.heading("时间", text="时间")
treeview.heading("价格", text="价格")


treeview.pack(side=LEFT, fill=BOTH)

sqlstr = "select * from  user "
s = cur.execute(sqlstr)
for row in s:
    treeview.insert('', 'end', values=(row[0],row[1],row[2],row[3]))




win.mainloop()
