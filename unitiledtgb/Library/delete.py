from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3

list1=[]
def mClick():
    a = txt1.get()

    conn = sqlite3.connect("d:/sql/library.db")
    cur = conn.cursor()
    sql_delete="delete from user where sid='%s'"%(a)
    sql_select = 'select sid from user'
    s = cur.execute(sql_select)

    for row in s:
        list1.append(row[0])
    if (a in list1):
        tkinter.messagebox.showinfo('删除图书信息', '删除成功！')
    else:
        tkinter.messagebox.showwarning('删除图书信息', '没有找到此书号，请重新输入')
    cur.execute(sql_delete)
    conn.commit()

    conn.close()
win=Toplevel()
win.geometry('300x300')
win.title("删除图书信息")

txt1=StringVar()

lab1=Label(win, text="请输入你想删除的图书书号：",font=('华文新魏','16'))
entry1 = Entry(win,textvariable=txt1, width=16,font=('宋体','16'))
button = Button(win, text='确认删除！',command=mClick, font=('宋体','16'))

lab1.grid(row=0,column=0)
entry1.grid(row=1,column=0)
button.grid(row=2,column=0)

win.mainloop()