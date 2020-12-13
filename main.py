import random

import flask
from flask import render_template

import gorilla

app = flask.Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def main():
    omikuji = [gorilla.no1, gorilla.no2, gorilla.no3, gorilla.no4, gorilla.no5, gorilla.no6,
               gorilla.no7, gorilla.no8, gorilla.no9, gorilla.no10, gorilla.no11, gorilla.no12,
               gorilla.no13, gorilla.no14, gorilla.no15, gorilla.no16, gorilla.no17, gorilla.no18,
               gorilla.no19, gorilla.no20, gorilla.no21, gorilla.no22, gorilla.no23, gorilla.no24,
               gorilla.no25]
    result = omikuji[random.randrange(len(omikuji))]
    return render_template('result.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
