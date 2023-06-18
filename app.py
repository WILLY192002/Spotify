import os
from flask import Flask, render_template, request, url_for, redirect


basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

@app.route('/')
def indexx():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)