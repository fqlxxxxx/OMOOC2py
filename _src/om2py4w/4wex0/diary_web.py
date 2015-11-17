# -*- coding: UTF-8 -*-


from bottle import route, run, jinja2_template, request, get, post

#从txt读取中文时不报错
import sys
reload(sys)
sys.setdefaultencoding('utf8')

'''
def read_diary():
    r = open("log.txt", "r")
    # rd = r.readline()
    # r.close()
        return line
'''

def read_history():
    r = open("log.txt", "r")
    rh = r.read()
    r.close()
    return rh


def writing(diary_content):
    w = open("log.txt", "a")
    w.write('%s ' % diary_content + "\n")
    w.close()


@route("/")
@route("/write_diary", method="POST")
def write_diary():
    diary_content = request.forms.get("content")
    writing(diary_content)
    #save_content = read_diary()
    diary_content = read_history()
    return jinja2_template('write_diary.html', diary_content=diary_content)


# 查看历史笔记
@route("/history")
def history():
    log_history = read_history()
    return jinja2_template('history.html', log_history=log_history)


run(host='localhost', port=8000, reloader=True)

