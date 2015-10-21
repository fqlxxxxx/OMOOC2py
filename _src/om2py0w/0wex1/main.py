#-*- coding: UTF-8 -*-

from sys import argv

script, text = argv

txt = open(text, 'w')


print "让我们开始日记吧!!!"
content = raw_input(">")


txt.write(content)

txt.close

print "已经保存日记"

