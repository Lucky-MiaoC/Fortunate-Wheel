'''此为后端代码，但主要功能均在前端实现'''

from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=False)
