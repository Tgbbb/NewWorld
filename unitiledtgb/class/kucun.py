from tkinter import *
from tkinter import ttk

win=Toplevel()
win.geometry('450x200')
win.title("库存信息")
lab1=Label(win, text="书号：",font=('华文新魏','16'))
lab2=Label(win, text="书名：",font=('华文新魏','16'))
lab3=Label(win, text="库存：",font=('华文新魏','16'))
lab5=Label(win, text="9787517042099",font=('华文新魏','16'))
lab6=Label(win, text="   Photoshop入门到创意 ",font=('华文新魏','16'))
lab7=Label(win, text="15",font=('华文新魏','16'))

lab1.grid(row=0,column=0)
lab2.grid(row=0,column=2)
lab3.grid(row=0,column=4)
lab5.grid(row=1,column=0)
lab6.grid(row=1,column=2)
lab7.grid(row=1,column=4)

win.mainloop()