# -*- coding: utf-8 -*-
# coding=utf-8, a = '中文'

from Tkinter import *
from os.path import exists

root = Tk()
root.title("极简日记本")


def save_text():
    t = entry.get()
    text.insert(END, t)
    # 一行显示一行
    text.insert(END, "\n")
    # 插入到显示区域后, 删除输入框中的文字
    entry.delete(0, END)
    l = open("log.txt", "a")
    # 解决编码问题
    l.write(t.encode("utf-8"))
    l.write("\n")
    l.close


text = Text(root, height=20, width=40)
entry = Entry(root, bg="gray")

buttonqiut = Button(root, text="退出", command=quit)
buttonadd = Button(root, text="保存", command=save_text)

if exists("log.txt"):
    L = open("log.txt", "r")
    r = L.read()
    text = Text(root)
    text.insert(END, r)
    L.close

text.pack()
entry.pack(side=LEFT)
buttonadd.pack(side=RIGHT)
buttonqiut.pack(side=RIGHT)
root.mainloop()