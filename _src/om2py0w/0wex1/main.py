#-*- coding: UTF-8 -*-



from sys import argv
from os.path import exists

script, text = argv



while True:
	input1 = raw_input("写吧:") 
	content = open(text, "a")
	content.write(input1)
	if input1 == "quit":
		input2 = raw_input("真要退出?Y/N")
		if input2 == "Y" or "y":
			break
			print "已退出并保存"
		else:
			continue

	


'''
#判断输入的日记名称是否重复,如果输入的日记名称已经存在, 可以继续追加
if exists(text) == True:
	print """
	#日记文档已经存在!!!
	#是否要补充此日记? 输入 y继续 n或"回车"退出
	"""
	judge1 = raw_input()

	#确认补充日记
	##Q为什么writelines写入时不能换行?
	if judge1 == "y":
		content1 = raw_input("补充日记:")
		txt1 = open(text, 'a')
		txt1.writelines(content1)
		txt1.close
		print "已经保存!"
	#如果不追加日记内容, 重新写日记
	else:
		print "退出!"

#如果日记文件名不重复,添加一条新纪录
else:
	print "让我们开始日记吧!!!"
	content = raw_input(">")

	txt = open(text, 'w')

	txt.write(content)

	txt.close

	print "已经保存!"


#查看历史日记

print "是否要查看其他日记? 输入 y继续 n或者\"回车\"退出 "


###Q如何命名变量,比如这个地方?
goon = raw_input("输入:")
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
'''



