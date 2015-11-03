#-*- coding: UTF-8 -*-


import socket

buffer = 1024
server_addr = ("localhost", 8888)
client_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    input = raw_input("请输入:")
    if input == "quit":
        print "您已退出日记!!"
        break
    client_s.sendto(input, server_addr)
    data, server_addr = client_s.recvfrom(buffer)
    print "收到:", data

client_s.close
