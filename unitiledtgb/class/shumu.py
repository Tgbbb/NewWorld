from tkinter import *
from tkinter import ttk

win=Toplevel()
win.geometry('450x200')
win.title("书目信息")

#文本
lab1=Label(win, text="书号：",font=('华文新魏','16'))
lab2=Label(win, text="书名：",font=('华文新魏','16'))
lab3=Label(win, text="出版时间：" ,font=('华文新魏','16'))
lab4=Label(win, text="价格：",font=('华文新魏','16'))
lab5=Label(win, text="9787517042099",font=('华文新魏','16'))
lab6=Label(win, text="   Photoshop入门到创意 ",font=('华文新魏','16'))
lab7=Label(win, text="2016-04-01",font=('华文新魏','16'))
lab8=Label(win, text="45.0",font=('华文新魏','16'))
#布局
lab1.grid(row=0,column=0)
lab2.grid(row=0,column=2)
lab3.grid(row=0,column=4)
lab4.grid(row=0,column=6)
lab5.grid(row=1,column=0)
lab6.grid(row=1,column=2)
lab7.grid(row=1,column=4)
lab8.grid(row=1,column=6)
win.mainloop()
