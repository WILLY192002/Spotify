from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL 
from config import config
from flask_login import LoginManager, login_user, logout_user, login_required

#Models
from models.ModelUser import ModelUser

#Entities
from models.entities.User import User



app = Flask(__name__)

db=MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)



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
    if request.method=='POST':
        user = User(0,0,request.form['username'],request.form['password'],0)
        logged_user = ModelUser.login(db,user)

        if logged_user != None:
            if logged_user.password:
                login_user(logged_user)
                return redirect(url_for('home'))
            else:
                flash("Contraseña Incorrecta")
                return render_template('auth/login.html')
        else:
            flash("Usuario no encontrado")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('home'))

    

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run()