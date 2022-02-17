from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.messagebox
import sqlite3

list1 = []

conn = sqlite3.connect("d:/sql/library.db")
cur = conn.cursor()

sql_select = 'select sid from user'
s = cur.execute(sql_select)

# for row in s:
#     list1.append(row)
#
# print(list1)

for row in s:
    list1.append(row[0])

# 注释，为什么这么写，1、用row去遍历cur.execute(sql_select)，每一个元素row取出来的是元组类型，row[0]就是取出row元组里的第一个字符串，就是我要的编号，再把这个字符串加入列表之中，就是这句话：list1.append(row[0])