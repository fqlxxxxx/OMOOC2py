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
