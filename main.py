import flask
from flask import render_template

import gorilla

app = flask.Flask(__name__)


@app.route('/')
def main():
    omikuji = gorilla.no1
    # result = omikuji[random.randint(0, len(omikuji))]
    return render_template('index.html', omikuji=omikuji)


if __name__ == '__main__':
    app.run(debug=True)
