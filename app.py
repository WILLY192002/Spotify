from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL 
from config import config
from flask_login import LoginManager, login_user, logout_user, login_required

#Models
from models.ModelUser import ModelUser
from models.ModelGenero import ModelGenero
from models.ModelCancion import ModelCanciones
from models.ModelSubida import ModelSubida

#Entities
from models.entities.User import User
from models.entities.Canciones import Canciones
from models.entities.Subida import Subida

#Operative System
import os



app = Flask(__name__)

db=MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)



@app.route('/')
def index():
    return redirect(url_for('home'))

@app.route('/user_<int:id_user>/upload-music', methods=['GET','POST'])
def upload(id_user):
    print("IDE USUARIO:",id_user)
    if request.method == 'POST':
        imagen = request.files['img_File'] #ESTE ES EL ARCHIVO
        autor = request.form['Aname']
        nombre = request.form['Sname']

        #PARA AGREGAR UN NUEVO GENERO
        genero = request.form.get('ListGen')
        if request.form['otherOption'] != "":
            genero =  request.form['otherOption']
            print("GENERO: |", genero,"|")
            #HACE LA INSERCIÓN EN BD
            ModelGenero.Insert(db,genero.upper())
            genero = ModelGenero.Select(db,'{}'.format(genero.upper()))[0].id

        #AGREGAR UNA NUEVA CANCION
        AddCancion = Canciones(0,nombre, autor, genero)
        ModelCanciones.agregar(db, AddCancion)
        idCancion = (ModelCanciones.filtrar(db, {'autor': '{}'.format(autor), 'nombre':'{}'.format(nombre)}))[0].id
        
        #AGRE NUEVA SUVIDA
        AddSubida = Subida(id_user, idCancion)
        ModelSubida.agregar(db, AddSubida)
        
        
            #GUARDAR LA IMAGEN CON AUTOR-NOMBRECANCION
        if imagen:
            ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
            ruta_destino = ruta_proyecto+'\static\img'
            nombre_archivo, extension = os.path.splitext(imagen.filename)
            print("NOMBRE ARCHIVO: ", nombre_archivo, "EXTENSIÓN: ", extension)
            imagen.save(os.path.join(ruta_destino, '{}-{}{}'.format(autor.capitalize(), nombre.capitalize(),extension)))

        #GUARDAR EL AUDIO CON AUTOR-NOMBRECANCION
        audio = request.files['mp3_File']
        ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
        ruta_destino = ruta_proyecto+'\static\music'
        audio.save(os.path.join(ruta_destino, '{}-{}.mp3'.format(autor.capitalize(), nombre.capitalize())))
        
        return redirect(url_for('home'))
    
    generos = ModelGenero.Select(db, "")
    return render_template('upload.html', id_user = id_user,generos = generos)

@app.route('/index', methods = ['GET', 'POST'])
def home():
    return render_template('index.html')

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    # Lógica para la página de registro
    if request.method == 'POST':
        password_hashed = User.set_password(request.form['password'])
        user = User(0, request.form['name'], request.form['email'], password_hashed, request.form['username'])
        success = ModelUser.register(db, user)

        if success:
            flash("¡Registro exitoso! Por favor, inicia sesión.")
            return redirect(url_for('login'))
        else:
            flash("Error en el registro. Por favor, intenta nuevamente.")
            return render_template('auth/register.html')
    
    else:
        return render_template('auth/register.html')
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    # Lógica para la página de inicio de sesión
    if request.method=='POST':
        user = User(0, 0,request.form['username'],request.form['password'],0)
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