import random
import flask
from flask import render_template

app = flask.Flask(__name__)


@app.route('/')
def main():
    omikuji = ["大吉", "吉", "中吉", "小吉", "末吉", "凶"]
    goribia = ["bia1", "bia2", "bia3", "bia4", "bia5", "bia6"]
    result = omikuji[random.randint(0, len(omikuji))]
    print(result)


if __name__ == '__main__':
    app.run(debug=True)
