#-*- coding: UTF-8 -*-
from bottle import route, run, jinja2_template
#from jinja2 import Environment, PackageLoader
# env = Environment(loader=PackageLoader('/templates'))

# 主页面
@route("/")
@route("/index")
def index():
    # template = env.get_template('index.html')
    return jinja2_template('base.html')

run(host='localhost', port=5000, reloader=True)


# 保存笔记


# 查看历史笔记页面





                 #@route('/hello/<name>')
                 # def hello(name='stranger'):
                 #    return template('Hello {{name}}, how are you?', name=name)
                 # run(host='localhost', port=8080)
