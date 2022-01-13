from tkinter import *
from tkinter import ttk
import tkinter

import tkinter.messagebox
import sqlite3

def mClick():
    a = txt1.get()
    return a

win = tkinter.Tk()
win.title('前程无忧爬虫系统')
win.geometry('300x400')
group = ttk.LabelFrame(win, text="前程无忧爬虫系统")
# 按钮
txt1=StringVar()
entry1 = Entry(group,textvariable=txt1,width=16,font=('宋体','16'))
button1 = Button(group, text='请输入你想要爬取的关键词',command=mClick)

# 布局
group.pack(padx=10, pady=10)
entry1.grid(row=0,column=2)
button1.grid(row=0, column=0)

win.mainloop()
b = mClick()
print(b)


