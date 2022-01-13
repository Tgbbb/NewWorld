from urllib import parse,request
from tkinter import *
from tkinter import ttk
import tkinter

#命令界面爬取数据
# def bug():
#     url = 'http://www.budejie.com/'
#
#     resp = request.urlopen(url)
#
#     print(resp.read().decode('utf-8'))
# print('请开启爬虫程序，启动为1，退出为0')
# a = int(input())
# if a == 1:
#     bug()
# else:
#     print('程序结束')

#图形界面爬取数据
def bug():
     url = 'http://www.budejie.com/'

     resp = request.urlopen(url)

     print(resp.read().decode('utf-8'))
win = tkinter.Tk()
win.title('Infinite爬虫')
win.geometry('300x300')

button1 = Button(win, text='爬取数据',command = bug)

button1.pack(padx=10, pady=10)

win.mainloop()
