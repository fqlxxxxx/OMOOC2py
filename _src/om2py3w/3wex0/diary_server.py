#-*- coding: UTF-8 -*-

import socket

buffer = 1024
server_addr = ("localhost", 8888)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(server_addr)

while True:
    print "正在同步数据"
    data, server_addr = s.recvfrom(buffer)
    print "同步以下数据:", data
    s.sendto(data, server_addr)
    print" 已经同步完毕!"
s.close
