# -*- coding: UTF-8 -*-


from Tkinter import *
from os.path import exists

root = Tk()
Frame(height=700, width=600, bg="white").pack()
# 修改 frame 窗体头部名称
root.title(" 极简日记本")
"""
# 读取历史日记, 未完成,没有定义 text
def writedarily():
    if exists(text):
        print "历史日记:"
        p = open(text, "r")
        print p.read()
"""
t = Text(root, bg="gray", height=600, width=400 )
t.pack
# 定义按钮
b = Button(text="写日记", bg="lightblue", height=2, width=6, command=writedarily)
b.place(x=100, y=20)

l = Label(root, height=20, width=70, text="2015年9月10日", fg="lightblue")
l.place(x=100, y=20)
root.mainloop()
