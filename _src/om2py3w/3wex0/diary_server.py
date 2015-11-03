#-*- coding: UTF-8 -*-

import socket
import datetime


buffer = 1024
server_addr = ("localhost", 8888)
server_s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_s.bind(server_addr)

while True:
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print "准备在同步数据..."
    data, client_addr = server_s.recvfrom(buffer)
    print "收到数据:", data + now
    L = open("log.txt", "a")
    L.write(data + now + "\n")
    L.close()
    server_s.sendto(data, client_addr)


server_s.close
