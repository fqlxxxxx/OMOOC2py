# -*- coding: UTF-8 -*-

from Tkinter import *
root = Tk()

Label(root,
      bg="red",
      text="Hello i am Tkinter"
      ).pack()

Label(root,
      bg="blue",
      text="Hello i am Tkinter"
      ).pack()

Label(root,
      text="我是",
      width=3,
      height=10,
      bg="blue"
      ).pack()

Label(root,
      text="日记本",
      width=20,
      height=3,
      bg="red"
      ).pack()

root.title("极简日记本")
root.mainloop()




