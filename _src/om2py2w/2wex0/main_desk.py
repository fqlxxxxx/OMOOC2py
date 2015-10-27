# -*- coding: UTF-8 -*-


from Tkinter import *
root = Tk()
Frame(height=700, width=600, bg="white").pack()
# 修改 frame 窗体头部名称
root.title(" 极简日记本")
Label(root, height=20, width=70, text="2015年9月10日", fg="lightblue").pack()
root.mainloop()
