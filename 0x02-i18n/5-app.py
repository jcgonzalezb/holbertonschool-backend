#!/usr/bin/env python3
"""
Script that starts a basic mock user login system
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


@app.route('/', methods=("GET", "POST"), strict_slashes=False)
def index():
    """Function that displays info from 5-index.html"""
    return render_template('5-index.html', locale=get_locale()
                           or babel.default_locale)


class Config(object):
    """flask app config Class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object('5-app.Config')


@babel.localeselector
def get_locale():
    """Function that determine the best match with supported languages"""
    locale = request.args.get('locale')
    if locale is not None and locale in Config.LANGUAGES:
        return locale
    else:
        return request.accept_languages.best_match(Config.LANGUAGES)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Function that returns an user dictionary"""
    user = request.args.get('login_as')
    key = int(user)
    if key is not None and key in users:
        return users[key]
    else:
        return None


@app.before_request
def before_request():
    """Function that returns an user dictionary"""
    user = get_user()
    g.user = user


if __name__ == '__main__':
    app.run(debug=True)
