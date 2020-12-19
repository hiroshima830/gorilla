# coding:utf-8
import os

from bottle import route, run


@route("/")
def hello_world():
    return "hello world"


if __name__ == '__main__':
    app.run(debug=True)
