from flask import Flask, render_template, request

from src.reducio import reducio

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reducio', methods=['POST'])
def test():
    article = str(request.form.get('text'))
    number = int(request.form.get('number'))

    return reducio(article, number)


if __name__ == '__main__':
    app.run()
