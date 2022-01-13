from tkinter import *
import tkinter.ttk as ttk

win = Tk()
win.title("Treeview 学习")

col = [1,2,3,4]
data = {"item0":["1a","2a","3a","4a"], "item1":{"num0":["1n", "2n", "3n"," 4n"],"num1":["1m","2m","3m","4m"]}, "item2":["1c","2c","3c","4c"]}

tree = ttk.Treeview(win, columns = col, height = 10, show = "tree")
#show = "tree", 第一列也会被显示出来
#也可用show = "headings" 把第一列隐藏起来
#height 的单位是字符，本例里可以显示10行

tree.column('0',width=150,anchor='center') #指定第一列的宽度和名称， 如果show = "headings", 这一列就被隐藏。
tree.column('1',width=100,anchor='center')
tree.column('2',width=100,anchor='w')
tree.column('3',width=100,anchor='center')
tree.column('4',width=100,anchor='center')
tree.heading('0',text='column0')
tree.heading('1',text='column1')
tree.heading('2',text='column2')
tree.heading('3',text='column3')
tree.heading('4',text='column4')

tree.insert('','end',values= data["item0"])
tree.insert('','end',values= data["item2"])

tree.pack()

win.mainloop()