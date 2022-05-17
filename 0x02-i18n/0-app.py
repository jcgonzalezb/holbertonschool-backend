#!/usr/bin/env python3
"""
Script that starts a basic Flask app
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', methods=("GET", "POST"), strict_slashes=False)
def index():
    """Function that displays Hello world'"""
    return "Hello world"

if __name__ == '__main__':
    app.run()