#!/usr/bin/python3
"""
This module starts a Flask web application
"""
from flask import Flask, render_template_string, abort

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
    Returns a string 'Python <text>' where <text> is replaced by
    the text variable,
    with underscores replaced by spaces. Defaults to 'is cool'
    if no text is provided.
    """
    return "Python " + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    """
    Returns a string '<n> is a number' if <n> is an integer
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Returns an HTML page with 'Number: <n>' if <n> is an integer
    """
    return render_template_string("""
    <!DOCTYPE html>
    <HTML lang="en">
        <HEAD>
            <TITLE>HBNB</TITLE>
        </HEAD>
        <BODY>
            <H1>Number: {{ n }}</H1>
        </BODY>
    </HTML>
    """, n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
