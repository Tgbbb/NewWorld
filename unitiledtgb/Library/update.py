from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3

win=Toplevel()
win.geometry('500x200')
win.title("修改图书信息")
list1=[]

def mClick():
    a = txt1.get()
    b = txt2.get()
    c = txt3.get()
    d = txt4.get()
    e = txt5.get()

    conn = sqlite3.connect("d:/sql/library.db")
    cur = conn.cursor()
    sql_update = "update user set name='%s',time='%s',jiage='%s',kucun='%s'where sid='%s'" % (b,c,d,e, a)
    sql_select = 'select sid from user'
    s=cur.execute(sql_select)

    for row in s:
        list1.append(row[0])
    if (a in list1):
        tkinter.messagebox.showinfo('修改图书信息', '修改成功！')
    else:
        tkinter.messagebox.showwarning('修改图书信息', '没有找到此书号，请重新输入')
    cur.execute(sql_update)
    conn.commit()

    conn.close()


group = ttk.LabelFrame(win,text="修改图书信息")
lab1=Label(group, text="请输入你要修改图书的书号：",font=('华文新魏','16'))
lab2=Label(group, text="修改后的书名：",font=('华文新魏','16'))
lab3=Label(group, text="修改后的出版时间：",font=('华文新魏','16'))
lab4=Label(group, text="修改后的价格：",font=('华文新魏','16'))
lab5=Label(group, text="修改后的库存：",font=('华文新魏','16'))

txt1=StringVar()
txt2=StringVar()
txt3=StringVar()
txt4=StringVar()
txt5=StringVar()

entry1 = Entry(group,textvariable=txt1, width=16,font=('宋体','16'))
entry2 = Entry(group,textvariable=txt2,width=16,font=('宋体','16'))
entry3 = Entry(group,textvariable=txt3, width=16,font=('宋体','16'))
entry4 = Entry(group,textvariable=txt4,width=16,font=('宋体','16'))
entry5 = Entry(group,textvariable=txt5, width=16,font=('宋体','16'))
button = Button(group, text='确认修改',command=mClick, font=('宋体','16'))

group.grid(row=0,column=0)
lab1.grid(row=0,column=0)
lab2.grid(row=1,column=0)
lab3.grid(row=2,column=0)
lab4.grid(row=3,column=0)
lab5.grid(row=4,column=0)
entry1.grid(row=0,column=1)
entry2.grid(row=1,column=1)
entry3.grid(row=2,column=1)
entry4.grid(row=3,column=1)
entry5.grid(row=4,column=1)
button.grid(row=5,column=1)

win.mainloop()
