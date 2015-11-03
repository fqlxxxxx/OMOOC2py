#-*- coding: UTF-8 -*-


import socket

buffer = 1024
client_addr = ("localhost", 8888)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    print "正在与服务器同步"
    input = raw_input("快来记录你的一天:")
    s.sendto(input, client_addr)
    data = s.recvfrom(buffer)
    print "同步完成"
s.close
