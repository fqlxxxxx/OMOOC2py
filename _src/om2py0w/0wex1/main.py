#-*- coding: UTF-8 -*-


from os.path import exists
import datetime  # 导入时间模块


while exists("log.txt"):
    print "历史日记:"
    p = open("log.txt", "r")
    print p.read()
    break

while True:
    print "添加新日记:"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 获取当前时间
    input1 = raw_input(">")
    if input1 == "quit":  # 调整代码位置解决 quit 写入 txt 中
        input2 = raw_input("真要退出?y/n:")
        if input2 == "y":
            print "已退出并保存"
            break
        if input2 == "n":
            continue

    content = open("log.txt", "a")
    content.write(input1 + now + "\n")
    # content.write("%s" % now)  # 另外一种将时间变为文本格式的方法, 记录时间, write 只能写入字符串, 日期无法直接写入, 因此用字符串替换的方式转换一下
    # content.write("\n")  # 解决写入日记换行问题
    content.close
