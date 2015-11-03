#-*- coding: UTF-8 -*-


import socket

buffer = 1024
client_addr = ("localhost", 8888)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    input = raw_input("请输入:")
    if input == "quit":
    	print "您已退出日记!!"
        break
    s.sendto(input, client_addr)
    data = s.recvfrom(buffer)
    print "收到:", data

s.close
