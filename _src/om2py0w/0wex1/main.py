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


#查看历史日记

print "是否要继续查看其他日记? 输入 y继续 n退出 "

###Q如何命名变量,比如这个地方
goon = raw_input("")
if goon == "y":

	txt = raw_input("请输入日记名称:")

	#判断输入的日记名是否存在
	judge = exists(txt)

	#如果True, 则显示日记内容
	#如果False, 则提示日记不存在
	if judge == True:
		print "%s的日记内容是:" % txt
		
		R = open(txt)

		print R.read()

		R.close
	else:
		print "您查询的日记不存在!"
else:
	print "退出日记"




