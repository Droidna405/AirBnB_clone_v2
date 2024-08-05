#!/usr/bin/python3
"""
This module starts a Flask web application
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Returns a string 'Hello HBNB!' when accessing the root URL
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Returns a string 'HBNB' when accessing the /hbnb URL
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Returns a string 'C <text>' where <text> is replaced by the text variable,
    with underscores replaced by spaces
    """
    return "C " + text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Returns a string 'Python <text>' where <text> is replaced by the
    text variable,
    with underscores replaced by spaces. Defaults to 'is cool'
    if no text is provided.
    """
    return "Python " + text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
