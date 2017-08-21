from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/test', methods=['POST'])
def test():
    with open('data/article.txt', 'w') as file:
        file.write(request.form.get('text'))


if __name__ == '__main__':
    app.run()
