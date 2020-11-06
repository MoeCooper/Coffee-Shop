from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def print_hi():
    return render_template('coffee.html')


if __name__ == '__main__':
    print_hi('PyCharm')
