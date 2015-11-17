# -*- coding: UTF-8 -*-


from bottle import route, run, jinja2_template, request, get, post
import datetime
import socket


#从txt读取中文时不报错
import sys
reload(sys)
sys.setdefaultencoding('utf8')




def read_history():
    r = open("log.txt", "r")
    rh = r.read()
    r.close()
    return rh


def writing(diary_content):
    w = open("log.txt", "a")
    now_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    w.write('%s ' % diary_content + now_time + "\n")
    w.close()



@route("/")
@route("/write_diary", method="POST")
def write_diary():
    diary_content = request.forms.get("content")
    writing(diary_content)
    diary_content = read_history()
    return jinja2_template('write_diary.html', diary_content=diary_content)

buffer = 1024
server_addr = ("localhost", 8000)
client_web = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    input = writing(diary_content)
    client_web.sendto(input, server_addr)
    client_web.recvfrom(buffer)
    print "已提交!"

client_web.close



run(host='localhost', port=8000, reloader=True)
