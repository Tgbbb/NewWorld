from tkinter import *
from tkinter import ttk
import sqlite3

win=Toplevel()
win.geometry('850x250')
win.title("图书库存管理系统")

def mClick():
  a=txt1.get()
  b=txt2.get()
  c=txt3.get()
  d=txt4.get()
  e=txt5.get()

  conn = sqlite3.connect("d:/sql/library.db")
  cur = conn.cursor()
  sqlstr = "insert into user(sid, name, time,jiage,kucun) values('%s','%s','%s','%s','%s')"%(a,b,c,d,e)
  cur.execute(sqlstr)
  conn.commit()
  conn.close()

  if(a != 0,b !=0, c!=0,d!=0,e!=0):
      txt6.set('添加图书成功')

photo=PhotoImage(file='P5.png')
labp=Label(win,image=photo)
group = ttk.LabelFrame(win,text="添加图书信息")
lab1=Label(group, text="书号：",font=('华文新魏','16'))
lab2=Label(group, text="书名：",font=('华文新魏','16'))
lab3=Label(group, text="出版时间：",font=('华文新魏','16'))
lab4=Label(group, text="价格：",font=('华文新魏','16'))
lab5=Label(group, text="库存：",font=('华文新魏','16'))
txt1=StringVar()
txt2=StringVar()
txt3=StringVar()
txt4=StringVar()
txt5=StringVar()
txt6=StringVar()
txt6.set("请添加图书")
entry1 = Entry(group,textvariable=txt1,width=16,font=('宋体','16'))
entry2 = Entry(group,textvariable=txt2,width=16,font=('宋体','16'))
entry3 = Entry(group,textvariable=txt3,width=16,font=('宋体','16'))
entry4 = Entry(group,textvariable=txt4,width=16,font=('宋体','16'))
entry5 = Entry(group,textvariable=txt5, width=16,font=('宋体','16'))
button = Button(group, text='提交', command=mClick,font=('宋体','16'))
lab6=Label(group,textvariable=txt6,relief='ridge',width=30,font=('华文新魏','16'))

#布局
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
lab6.grid(row=5, column=0,)
button.grid(row=5,column=1)
labp.grid(row=0,column=2)



win.mainloop()