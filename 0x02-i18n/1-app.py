#!/usr/bin/env python3
"""
Script that starts a basic flask Babel setup
"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=("GET", "POST"), strict_slashes=False)
def index():
    """Function that displays info from 1-index.html"""
    return render_template('1-index.html')


class Config(object):
    """flask app config Class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('1-app.Config')
#app.config['BABEL_DEFAULT_LOCALE'] = 'en'
#app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'

if __name__ == '__main__':
    app.run()
