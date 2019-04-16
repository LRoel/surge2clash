from flask import Flask
from flask import request
from main import Surge3
from main import Clash

app = Flask(__name__)


@app.route('/surge')
def surge():
    return Surge3(request)


@app.route('/clash')
def clash():
    return Clash(request)


if __name__ == '__main__':
    app.run()
