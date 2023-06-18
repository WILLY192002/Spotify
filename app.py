import os
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL 
from config import config

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

db=MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/index', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    # Lógica para la página de registro
    return render_template('auth/login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Lógica para la página de inicio de sesión
    return render_template('auth/login.html')

if __name__ == '__main__':
    app.run(debug=True)