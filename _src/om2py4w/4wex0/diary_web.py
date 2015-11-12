# -*- coding: UTF-8 -*-


from bottle import route, run, jinja2_template, request, get, post


# 主页面
@route("/")
@route("/index")
def index():
    return jinja2_template('index.html')


# 写日记页面
@route("/write_diary")
@get("/write_diary")
def write_diary_form():
    return jinja2_template('write_diary.html')


@route("/write_diary")
@post("/write_diary")
def write_diary():
    diary_content = request.forms.get('diary_content')
    return jinja2_template('write_diary.html', diary_content=diary_content)



# 查看历史笔记
@route("/history")
def history():
    return jinja2_template('history.html')


run(host='localhost', port=5000, reloader=True)

