#-*- coding: UTF-8 -*-



from sys import argv
from os.path import exists

script, text = argv

txt = open(text, 'w')


print "让我们开始日记吧!!!"
content = raw_input(">")


txt.write(content)

txt.close

print "已经保存日记"


print "是否要继续查看其他日记? 点击回车继续! 退出 control+C"

raw_input(">")

txt = raw_input("请输入日记名称:")

print "日记是否存在? %r" % exists(txt)

R = open(txt)

print R.read()

R.close






