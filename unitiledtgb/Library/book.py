from tkinter import *
from tkinter import ttk
import tkinter
import tkinter.messagebox
import sqlite3

#书目信息
def shumu():
    conn = sqlite3.connect("d:/sql/library.db")
    cur = conn.cursor()

    win = Toplevel()
    win.geometry('570x200')
    win.title("书目信息")

    columns = ("编号", "书名", "时间", "价格")
    treeview = ttk.Treeview(win, height=20, show='headings', columns=columns)

    treeview.column("编号", width=200, anchor='center')
    treeview.column("书名", width=200, anchor='center')
    treeview.column("时间", width=100, anchor='center')
    treeview.column("价格", width=70, anchor='center')

    treeview.heading("编号", text="编号")  # 显示表头
    treeview.heading("书名", text="书名")
    treeview.heading("时间", text="时间")
    treeview.heading("价格", text="价格")

    treeview.pack(side=LEFT, fill=BOTH)

    sqlstr = "select * from  user "
    s = cur.execute(sqlstr)
    for row in s:
        treeview.insert('', 'end', values=(row[0], row[1], row[2], row[3]))

    win.mainloop()
#添加图书信息
def tianjia():
    win = Toplevel()
    win.geometry('850x250')
    win.title("图书库存管理系统")

    def mClick():
        a = txt1.get()
        b = txt2.get()
        c = txt3.get()
        d = txt4.get()
        e = txt5.get()

        conn = sqlite3.connect("d:/sql/library.db")
        cur = conn.cursor()
        sqlstr = "insert into user(sid, name, time,jiage,kucun) values('%s','%s','%s','%s','%s')" % (a, b, c, d, e)
        cur.execute(sqlstr)
        conn.commit()
        conn.close()

        if (a != 0, b != 0, c != 0, d != 0, e != 0):
            txt6.set('添加图书成功')

    photo = PhotoImage(file='P5.png')
    labp = Label(win, image=photo)
    group = ttk.LabelFrame(win, text="添加图书信息")
    lab1 = Label(group, text="书号：", font=('华文新魏', '16'))
    lab2 = Label(group, text="书名：", font=('华文新魏', '16'))
    lab3 = Label(group, text="出版时间：", font=('华文新魏', '16'))
    lab4 = Label(group, text="价格：", font=('华文新魏', '16'))
    lab5 = Label(group, text="库存：", font=('华文新魏', '16'))
    txt1 = StringVar()
    txt2 = StringVar()
    txt3 = StringVar()
    txt4 = StringVar()
    txt5 = StringVar()
    txt6 = StringVar()
    txt6.set("请添加图书")
    entry1 = Entry(group, textvariable=txt1, width=16, font=('宋体', '16'))
    entry2 = Entry(group, textvariable=txt2, width=16, font=('宋体', '16'))
    entry3 = Entry(group, textvariable=txt3, width=16, font=('宋体', '16'))
    entry4 = Entry(group, textvariable=txt4, width=16, font=('宋体', '16'))
    entry5 = Entry(group, textvariable=txt5, width=16, font=('宋体', '16'))
    button = Button(group, text='提交', command=mClick, font=('宋体', '16'))
    lab6 = Label(group, textvariable=txt6, relief='ridge', width=30, font=('华文新魏', '16'))

    # 布局
    group.grid(row=0, column=0)
    lab1.grid(row=0, column=0)
    lab2.grid(row=1, column=0)
    lab3.grid(row=2, column=0)
    lab4.grid(row=3, column=0)
    lab5.grid(row=4, column=0)
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    entry3.grid(row=2, column=1)
    entry4.grid(row=3, column=1)
    entry5.grid(row=4, column=1)
    lab6.grid(row=5, column=0, )
    button.grid(row=5, column=1)
    labp.grid(row=0, column=2)

    win.mainloop()
#库存信息
def kucun():
    conn = sqlite3.connect("d:/sql/library.db")
    cur = conn.cursor()

    win = Toplevel()
    win.geometry('500x200')
    win.title("书目信息")

    columns = ("编号", "书名", "库存")
    treeview = ttk.Treeview(win, height=20, show='headings', columns=columns)

    treeview.column("编号", width=200, anchor='center')
    treeview.column("书名", width=200, anchor='center')
    treeview.column("库存", width=100, anchor='center')

    treeview.heading("编号", text="编号")
    treeview.heading("书名", text="书名")
    treeview.heading("库存", text="库存")

    treeview.pack(side=LEFT, fill=BOTH)

    sqlstr = "select * from  user"
    s = cur.execute(sqlstr)
    for row in s:
        treeview.insert('', 'end', values=(row[0], row[1], row[4]))

    win.mainloop()
#修改信息
def update():
    win = Toplevel()
    win.geometry('500x200')
    win.title("修改图书信息")
    list1 = []

    def mClick():
        a = txt1.get()
        b = txt2.get()
        c = txt3.get()
        d = txt4.get()
        e = txt5.get()

        conn = sqlite3.connect("d:/sql/library.db")
        cur = conn.cursor()
        sql_update = "update user set name='%s',time='%s',jiage='%s',kucun='%s'where sid='%s'" % (b, c, d, e, a)
        sql_select = 'select sid from user'
        s = cur.execute(sql_select)

        for row in s:
            list1.append(row[0])
        if (a in list1):
            tkinter.messagebox.showinfo('修改图书信息', '修改成功！')
        else:
            tkinter.messagebox.showwarning('修改图书信息', '没有找到此书号，请重新输入')
        cur.execute(sql_update)
        conn.commit()

        conn.close()

    group = ttk.LabelFrame(win, text="修改图书信息")
    lab1 = Label(group, text="请输入你要修改图书的书号：", font=('华文新魏', '16'))
    lab2 = Label(group, text="修改后的书名：", font=('华文新魏', '16'))
    lab3 = Label(group, text="修改后的出版时间：", font=('华文新魏', '16'))
    lab4 = Label(group, text="修改后的价格：", font=('华文新魏', '16'))
    lab5 = Label(group, text="修改后的库存：", font=('华文新魏', '16'))

    txt1 = StringVar()
    txt2 = StringVar()
    txt3 = StringVar()
    txt4 = StringVar()
    txt5 = StringVar()

    entry1 = Entry(group, textvariable=txt1, width=16, font=('宋体', '16'))
    entry2 = Entry(group, textvariable=txt2, width=16, font=('宋体', '16'))
    entry3 = Entry(group, textvariable=txt3, width=16, font=('宋体', '16'))
    entry4 = Entry(group, textvariable=txt4, width=16, font=('宋体', '16'))
    entry5 = Entry(group, textvariable=txt5, width=16, font=('宋体', '16'))
    button = Button(group, text='确认修改', command=mClick, font=('宋体', '16'))

    group.grid(row=0, column=0)
    lab1.grid(row=0, column=0)
    lab2.grid(row=1, column=0)
    lab3.grid(row=2, column=0)
    lab4.grid(row=3, column=0)
    lab5.grid(row=4, column=0)
    entry1.grid(row=0, column=1)
    entry2.grid(row=1, column=1)
    entry3.grid(row=2, column=1)
    entry4.grid(row=3, column=1)
    entry5.grid(row=4, column=1)
    button.grid(row=5, column=1)

    win.mainloop()
#删除信息
def delete():
    list1 = []

    def mClick():
        a = txt1.get()

        conn = sqlite3.connect("d:/sql/library.db")
        cur = conn.cursor()
        sql_delete = "delete from user where sid='%s'" % (a)
        sql_select = 'select sid from user'
        s = cur.execute(sql_select)

        for row in s:
            list1.append(row[0])
        if (a in list1):
            tkinter.messagebox.showinfo('删除图书信息', '删除成功！')
        else:
            tkinter.messagebox.showwarning('删除图书信息', '没有找到此书号，请重新输入')
        cur.execute(sql_delete)
        conn.commit()

        conn.close()

    win = Toplevel()
    win.geometry('300x300')
    win.title("删除图书信息")

    txt1 = StringVar()

    lab1 = Label(win, text="请输入你想删除的图书书号：", font=('华文新魏', '16'))
    entry1 = Entry(win, textvariable=txt1, width=16, font=('宋体', '16'))
    button = Button(win, text='确认删除！', command=mClick, font=('宋体', '16'))

    lab1.grid(row=0, column=0)
    entry1.grid(row=1, column=0)
    button.grid(row=2, column=0)

    win.mainloop()
#主界面
print("=" * 20)
print("图书库存管理系统V0.1")
print("1.显示书目信息")
print("2.显示图书库存信息")
print("3.添加书目信息")
print("4.修改图书库存量")
print("5.退出系统")
print("=" * 20)

win = tkinter.Tk()
win.title('图书库存管理系统V1.0内测版')
win.geometry('300x400')
group = ttk.LabelFrame(win, text="图书库存管理系统")
# 按钮
button1 = Button(group, text='显示书目信息', command=shumu)
button2 = Button(group, text='显示库存信息', command=kucun)
button3 = Button(group, text='添加书目信息', command=tianjia)
button5 = Button(group, text='修改图书信息', command=update)
button6 = Button(group, text='删除图书信息', command=delete)
button4 = Button(group, text='退出', command=win.quit)

# 事件

# 布局
group.pack(padx=10, pady=10)
button1.grid(row=0, column=0)
button2.grid(row=1, column=0)
button3.grid(row=2, column=0, )
button5.grid(row=3, column=0, )
button6.grid(row=4, column=0, )
button4.grid(row=5, column=0)

win.mainloop()


