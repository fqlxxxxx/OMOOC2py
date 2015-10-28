# -*- coding: utf-8 -*-


from Tkinter import *  # import Tkinter module

#


class Application(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.mydarily()

    def mydarily(self):
        # 添加显示区域
        self.text = Text(self, bg="gray", height=600, width=400)
        self.text.pack()
        # 添加输入框
        self.entry = Entry(self)
        self.entry.pack()
        # 添加添加按钮和退出按钮
        self.buttonadd = Button(self, text="添加")
        self.buttonadd.pack()
        self.buttonquit = Button(self, text="退出")
        self.buttonquit.pack()

app = Application()
app.master.title("极简日记本")
app.mainloop()