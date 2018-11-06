from flask import Flask
from flask import request, jsonify, render_template, Flask
import logging

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
app = Flask(__name__)


@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/')
def home():
    LOG.debug('Hit landing page.')
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
