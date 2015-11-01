# -*- coding: utf-8 -*-
# -*- coding: UTF-8 -*-

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
    l.write(t)
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


'''
class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.mydarily()

    def mydarily(self):
        # 添加显示区域
        self.text = Text(self, height=20, width=40, state=DISABLED)
        self.text.pack()

        # 添加输入框
        self.entry = Entry(self, bg="blue")
        self.entry.pack(side=LEFT)

    def text(self):
        t = self.entry.get()
        self.text.insert(0, t)      

        # 添加退出按钮
    def mydarily(self):
        self.buttonquit = Button(self, text="退出", command=self.quit)
        self.buttonquit.pack(side=RIGHT)

        # 添加保存按钮
    def mydarily(self):
        self.buttonadd = Button(self, text="保存", command=self.text)
        # 绑定按钮
        self.buttonadd.bind()
        self.buttonadd.pack(side=RIGHT)

app = Application()
app.master.title("极简日记本")

app.mainloop()
'''
