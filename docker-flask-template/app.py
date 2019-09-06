
from flask import request, jsonify, render_template, Flask
import logging
import time

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)
LOG.setLevel(logging.DEBUG)
app = Flask(__name__)
SERVICE_VERSION="0.0.1"
INTERFACE_VERSION="0.0.1"

METHOD = 'method'

@app.route('/hello')
def hello_world():
    return 'Hello World!'


@app.route('/')
def home():
    LOG.debug('Hit landing page.')
    return render_template('home.html', methodname=METHOD, 
                           version=SERVICE_VERSION,
                           interface_version=INTERFACE_VERSION)


@app.route(f"/{METHOD}/", methods=['POST'])
def method():
    data = request.get_json(force=True)
    LOG.debug('Testing the method.')
    time.sleep(2)
    txt = data['text']
    return txt.lower()


@app.route("/blurgh/")
def blurgh():
    LOG.debug('Testing the blurgh.')
    return 'blurgh'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
