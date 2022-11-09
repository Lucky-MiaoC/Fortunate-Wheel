'''此为后端代码，但主要功能均在前端实现'''

import sys
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
    port = int(sys.argv[1]) if len(sys.argv) >= 2 else 5000
    app.run(host='127.0.0.1', port=port, debug=False)
