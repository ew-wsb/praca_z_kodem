from flask import Flask
APP = Flask(__name__)


@APP.route('/')
def index():
    """<h1>Hello WSB! Greetings from Flask $ Docker!</h1>"""

if __name__ == '__main__':
    APP.run(debug=True)
