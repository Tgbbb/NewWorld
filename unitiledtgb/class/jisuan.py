from tkinter import *
from tkinter import ttk
import tkinter

win=tkinter.Tk()
win.geometry('600x200')
win.title("加法计算器")

def mClick():
    txt=txt1.get()
    Txt=txt2.get()
    txt3.set(txt+Txt)

txt1=IntVar()
txt2=IntVar()
txt3=StringVar()
label=Label(win,text='  +  ')
entry1 = Entry(win,textvariable=txt1, width=4,font=('宋体','16') )
entry2 = Entry(win,textvariable=txt2,width=4,font=('宋体','16'))
entry3=Entry(win,width=4,textvariable=txt3,font=('华文新魏','16'))
button = Button(win, text='=',command=mClick,font=('宋体','16'))

entry1.grid(row=0,column=0)
entry2.grid(row=0,column=2)
entry3.grid(row=0,column=6)
button.grid(row=0,column=4)
label.grid(row=0,column=1)
win.mainloop()