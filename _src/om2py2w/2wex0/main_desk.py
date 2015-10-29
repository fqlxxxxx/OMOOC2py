# -*- coding: utf-8 -*-


from Tkinter import *  # import Tkinter module


def save_text():
    t = entry.get()
    text.insert(END, t)

root = Tk()
root.title("极简日记本")

text = Text(root, height=20, width=40)
entry = Entry(root, bg="gray")

buttonqiut = Button(root, text="退出", command=quit)
buttonadd = Button(root, text="保存", command=save_text)

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
