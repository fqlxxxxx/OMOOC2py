# -*- coding: utf-8 -*-



'''


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.mydarily()

    def mydarily(self):
        # 添加显示区域
        self.text = Text(self, bg="gray", height=20, width=40)
        self.text.pack()
        # 添加退出按钮
        self.buttonquit = Button(self, text="退出", command=self.quit)
        self.buttonquit.pack(side=RIGHT)
        # 添加保存按钮
        self.buttonadd = Button(self, text="保存")
        # 绑定按钮
        self.buttonadd.bind()
        self.buttonadd.pack(side=RIGHT)
        # 添加输入框
        self.entry = Entry(self, bg="blue")
        g = self.entry.get()
        self.entry.pack(side=LEFT)


app = Application()
app.master.title("极简日记本")

app.mainloop()

'''

from Tkinter import *

def app_text():
        text = e2.get()
        e1.insert(END, text)

def ins_text():
        text = e2.get()
        e1.insert(0, text)

def clr_text():
        e1.delete(0, END)

root = Tk()

e1 = Entry()
e2 = Entry()
b1 = Button(text = "Append Text", command = app_text)
b2 = Button(text = "Insert Text", command = ins_text)
b3 = Button(text = "Clear Text", command = clr_text)

e1.pack(padx = 10, pady = 10, fill = X)
e2.pack(padx = 10, pady = 10, fill = X)
b1.pack(padx = 10, pady = 5)
b2.pack(padx = 10, pady = 5)
b3.pack(padx = 10, pady = 5)

root.mainloop()