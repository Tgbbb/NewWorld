from tkinter import *
import tkinter
import tkinter.messagebox
win = tkinter.Tk()
win.title('画布示例')
win.geometry('250x300')
can=tkinter.Canvas(win,height=250,width=250)

def Click1():
    io1 = can.create_oval(35, 30, 210, 210, outline='pink', fill='pink')
    io2 = can.create_oval(70, 70, 180, 180, outline='red', fill='red')
    io3 = can.create_oval(65, 70, 185, 170, outline='pink', fill='pink')
    io4 = can.create_oval(80, 100, 110, 130, outline='blue', fill='blue')
    io5 = can.create_oval(150, 100, 180, 130, outline='blue', fill='blue')

#button
button1 = Button(win, text='退出',command=win.quit)
button2 = Button(win, text='请画一个笑脸',command=Click1)


button1.pack(side='bottom')
button2.pack(side='top')
can.pack()
win.mainloop()