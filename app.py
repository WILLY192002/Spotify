from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL 
from config import config
from flask_login import LoginManager, login_user, logout_user, login_required

#Models
from models.ModelUser import ModelUser
from models.ModelGenero import ModelGenero
from models.ModelCrearTabla import ModelCrearTabla
from models.ModelAddToUser import ModelAddToUser 

#Entities
from models.entities.User import User

from models.entities.TablaUser import TablaUser

#Operative System
import os

#Aux
from auxiliares import *



app = Flask(__name__)

db=MySQL(app)
login_manager_app = LoginManager(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(db, id)



@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/User_<int:id_user>/edit-song/Reg_<int:id_reg>', methods=['GET','POST'])
def editSong(id_user, id_reg):
    #action='/User_{{subida.usuario_id}}/edit-song/{{subida.id}}'
    if request.method == 'POST':
        id_registro = request.form['edtId']
        nombreAnterior = ModelAddToUser.Select(db, id_user, {'id':id_registro})
        ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
        nombrecancion = request.form['edtnombrecancion']
        autor = request.form['edtautor']
        imagen = request.files['edtimg']
        genero = request.form.get('edtlistgen')
        cambios = {}

        #Verificar si el genero es nuevo o si ya estaba
        if request.form['edtotheroption'] != "":
            genero =  request.form['edtotheroption']
            #VERIFICA Y HACE LA INSERCIÓN EN BD 
            VerificacionGenero = verificarGenero(db, '{}'.format(genero.upper()))
            if VerificacionGenero == False:
                ModelGenero.Insert(db,genero.upper())
                genero = verificarGenero(db, '{}'.format(genero.upper()))[0].id
                
            else:
                genero = VerificacionGenero[0].id
        cambios['genero_id'] = genero
        
        #GUARDAR LA IMAGEN CON AUTOR-NOMBRECANCION
        if imagen and nombreAnterior[0].foto:
            ruta_destinoImg = ruta_proyecto+'\static\img\{}'.format('ImgUser_'+(str(id_user)))
            borrarArchivo(ruta_destinoImg+'\{}-{}.PNG'.format(nombreAnterior[0].autor,nombreAnterior[0].nombrecancion))
            subirImagen(autor, nombrecancion, ruta_destinoImg, imagen)
            imagen = True
        elif imagen and nombreAnterior[0].foto == False:
            ruta_destinoImg = ruta_proyecto+'\static\img\{}'.format('ImgUser_'+(str(id_user)))
            subirImagen(autor, nombrecancion, ruta_destinoImg, imagen)
            imagen = True
        else:
            print("ENTRA DONDE NO CREIA")
            imagenAnterior = nombreAnterior[0].autor+'-'+nombreAnterior[0].nombrecancion+'.PNG'
            ruta_destinoImg = ruta_proyecto+'\static\img\{}\{}'.format('ImgUser_'+(str(id_user)), imagenAnterior)
            nuevonombre = ruta_proyecto+'\static\img\{}\{}'.format('ImgUser_'+(str(id_user)), autor+'-'+nombrecancion+'.PNG')
            renombrarArchivo(ruta_destinoImg, nuevonombre)
            imagen = True
        

        if nombrecancion != "" and autor != "":
            #ACTUALIZAMOS LA BD
            cambios['nombrecancion'] = nombrecancion
            cambios['autor'] = autor
            ModelAddToUser.EditToUser(db,id_registro,id_user, cambios)

            #ACTUALIZAR EL NOMBRE DEL ARCHIVO AUDIO
            ruta_destinoAud = ruta_proyecto+'\static\music\{}\{}'.format('MusicUser_'+(str(id_user)), nombreAnterior[0].autor+'-'+nombreAnterior[0].nombrecancion+'.mp3')
            nuevonombre = ruta_proyecto+'\static\music\{}\{}'.format('MusicUser_'+(str(id_user)), autor+'-'+nombrecancion+'.mp3')
            renombrarArchivo(ruta_destinoAud, nuevonombre)

        return redirect(url_for('gestionar', id_user = id_user))
    else:
        recuperada = ModelAddToUser.Select(db, id_user, {'id': id_reg})
        generos = ModelGenero.Select(db, "")
        return render_template('editSong.html', generos = generos, subida = recuperada[0])

@app.route('/gestion-canciones/User_<int:id_user>', methods=['GET','POST'])
def gestionar(id_user):
    if request.method == 'POST':
        print("entró a gestionar 1")
        id_registro = request.form['edtId2']
        versionAnterior = ModelAddToUser.Select(db, id_user, {'id':id_registro})
        ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
        ruta_destinoImg = ruta_proyecto+'\static\img\{}'.format('ImgUser_'+(str(id_user)))
        ruta_destinoAud = ruta_proyecto+'\static\Music\{}'.format('MusicUser_'+(str(id_user)))
        ModelAddToUser.deleteToUser(db,id_registro,id_user)
        borrarArchivo(ruta_destinoImg+'\{}-{}.PNG'.format(versionAnterior[0].autor,versionAnterior[0].nombrecancion))
        borrarArchivo(ruta_destinoAud+'\{}-{}.mp3'.format(versionAnterior[0].autor,versionAnterior[0].nombrecancion))
        return redirect(url_for('gestionar', id_user = id_user))
    elif request.method == 'GET':
        print("entró a gestionar 2")
        genero = request.args.get('BusquedaGen')
        nombre = request.args.get('BusquedaNom')
        print(genero, nombre)
        if genero == None:
            genero = ""
        if nombre == None:
            nombre =""
        filtro = {}

        print("FILTROS",nombre,"||",genero)
        if nombre != "" and genero != "":
            print("Entrooo1")
            print("Entrooo1",nombre,"||",genero)
            filtro = {'nombrecancion':nombre, 'autor':nombre, 'genero_id':genero}
        elif nombre != "":
            print("Entrooo2")
            print("Entrooo2",nombre,"||",genero)
            filtro = {'nombrecancion':nombre, 'autor':nombre}
        elif genero != "":
            print("Entrooo3")
            print("Entrooo3",nombre,"||",genero)
            filtro = {'genero_id':genero}
        
        recuperadas = ModelAddToUser.filter(db, id_user, filtro)
        generos = ModelGenero.Select(db,{})
        return render_template('gestion.html', subidas = recuperadas, generos = generos, id_user = id_user)
    else:
        print("Gestionar 3")

@app.route('/user_<int:id_user>/upload-music', methods=['GET','POST'])
def upload(id_user):
    print("IDE USUARIO:",id_user)
    if request.method == 'POST':
        imagen = request.files['img_File'] #ESTE ES EL ARCHIVO
        audio = request.files['mp3_File']
        autor = request.form['Aname']
        nombre = request.form['Sname']
        ruta_proyecto = os.path.dirname(os.path.abspath(__file__))
        genero = request.form.get('ListGen')

        #GUARDAR LA IMAGEN CON AUTOR-NOMBRECANCION
        if imagen:
            ruta_destinoImg = ruta_proyecto+'\static\img\{}'.format('ImgUser_'+(str(id_user)))
            subirImagen(autor, nombre, ruta_destinoImg, imagen)
            imagen = True
        else:
            imagen = False

        #GUARDAR EL AUDIO CON AUTOR-NOMBRECANCION
        ruta_destinoAud = ruta_proyecto+'\static\music\{}'.format('MusicUser_'+(str(id_user)))
        subirAudio(autor,nombre,ruta_destinoAud,audio)
        
        #PARA AGREGAR UN NUEVO GENERO
        if request.form['otherOption'] != "":
            genero =  request.form['otherOption']

            #VERIFICA Y HACE LA INSERCIÓN EN BD 
            VerificacionGenero = verificarGenero(db, '{}'.format(genero.upper()))
            if VerificacionGenero == False:
                ModelGenero.Insert(db,genero.upper())
                genero = verificarGenero(db, '{}'.format(genero.upper()))[0].id
            else:
                genero = VerificacionGenero[0].id
        
        Tablauser = ModelAddToUser.Select(db, id_user, {'autor': autor, 'nombrecancion':nombre})
        print("ESTO ES: ", Tablauser)
        if len(Tablauser) == 0:
            ModelAddToUser.AddToUser(db,id_user,nombre.capitalize(),autor.capitalize(),genero, imagen, False)

        #AGREGAR UNA NUEVA CANCION Y VERIFICAR SI EXISTE
        # AddCancion = Canciones(0,nombre.capitalize(), autor.capitalize(), genero, imagen)
        # VerificacionCancion = verificarCancion(db, {'autor': '{}'.format(autor), 'nombre':'{}'.format(nombre)})
        # idCancion = 0
        # if VerificacionCancion:
        #     idCancion = VerificacionCancion[0].id
        # else:
        #     ModelCanciones.agregar(db, AddCancion)
        #     idCancion = verificarCancion(db, {'autor': '{}'.format(autor), 'nombre':'{}'.format(nombre)})[0].id
        
        
        # #AGRE NUEVA SUVIDA
        # VerificacionSubida = verificarSubida(db, [id_user, idCancion])
        # if VerificacionSubida == False:
        #     AddSubida = Subida(id_user, idCancion)
        #     ModelSubida.agregar(db, AddSubida)
        
        return redirect(url_for('home', id_user = id_user))
    
    generos = ModelGenero.Select(db, "")
    return render_template('upload.html', id_user = id_user,generos = generos)

@app.route('/index/User_<int:id_user>/autor=<string:autor>/namesong=<string:nombre>/filterby/ftl1=<string:buscar>/ftl2=<int:idgen>', methods = ['GET'])
def filtrar(id_user,autor,nombre,buscar,idgen):
    if request.method == 'GET' and (buscar == ' ' and idgen == 0):
        print("SI ENTRO A FILTERer", buscar, "/",idgen)
        genero_id = request.args.get('BusquedaGen')
        nombre_autor = request.args.get('BusquedaNom')
        print("SI ENTRO A FILTER", genero_id, "/",nombre_autor)
        if buscar == ' ':
            print("CLARO Q YES")
        
        if genero_id == "" or genero_id == None:
            genero_id = 0
        
        if nombre_autor == "" or nombre_autor == None:
            nombre_autor = ' '
        filtros = {}
        if (genero_id != 0 and nombre_autor != ' '):
            filtros = {'nombrecancion': nombre_autor, 'autor': nombre_autor, 'genero_id':genero_id}
        elif (genero_id != 0 and nombre_autor == ' '):
            filtros = {'genero_id':genero_id}
        elif genero_id == 0 and nombre_autor != ' ':
            filtros = {'nombrecancion': nombre_autor, 'autor': nombre_autor}

        print("FILTROS", filtros)
        filter_songs = ModelAddToUser.filter(db,id_user,filtros)
        allGeneros = ModelGenero.Select(db,{})
        return render_template('index.html', recuperadas = filter_songs, generos = allGeneros, autor = autor, nombre = nombre, user = id_user, buscar=nombre_autor, idgen=genero_id)
    elif request.method == 'GET' and (buscar != ' ' or idgen != 0):
        print("SI ENTRO A FILTER2", buscar, "/", idgen)
        filtros = {}
        if (idgen != 0 and buscar != ' '):
            filtros = {'nombrecancion': buscar, 'autor': buscar, 'genero_id':idgen}
        elif (idgen != 0 and buscar == ' '):
            filtros = {'genero_id':idgen}
        else:
            filtros = {'nombrecancion': buscar, 'autor': buscar}

        print("FILTROS2", filtros)
        filter_songs = ModelAddToUser.filter(db,id_user,filtros)
        allGeneros = ModelGenero.Select(db,{})
        return render_template('index.html', recuperadas = filter_songs, generos = allGeneros, autor = autor, nombre = nombre, user = id_user, buscar=buscar, idgen=idgen)
    """ else:
        print("ENTRO AKI VIDA SUPER")
        filter_songs = ModelAddToUser.filter(db,id_user,{})
        allGeneros = ModelGenero.Select(db,{})
        return render_template('index.html', recuperadas = filter_songs, generos = allGeneros, autor = "", nombre = "", user = id_user, buscar=' ', idgen=0)
 """

@app.route('/index/User_<int:id_user>')
def home(id_user):
    Mysongs = ModelAddToUser.filter(db,id_user,{})
    allGeneros = ModelGenero.Select(db,{})
    return render_template('index.html', recuperadas = Mysongs, generos = allGeneros, autor = "", nombre = "", user = id_user, buscar=' ', idgen=0)
    



    """ if id_user != 0:
        genero = request.args.get('BusquedaGen')
        nombre = request.args.get('BusquedaNom')
        if genero == None:
            genero = ""
        if nombre == None:
            nombre =""
        filtro = {}

        if id_gen:
            filtro = {'genero_id':id_gen}
        else:
            if nombre != "" and genero != "":
                print("Entrooo1")
                print("Entrooo1",nombre,"||",genero)
                filtro = {'nombrecancion':nombre, 'autor':nombre, 'genero_id':genero}
            elif nombre != "":
                print("Entrooo2")
                print("Entrooo2",nombre,"||",genero)
                filtro = {'nombrecancion':nombre, 'autor':nombre}
            elif genero != "":
                print("Entrooo3")
                print("Entrooo3",nombre,"||",genero)
                filtro = {'genero_id':genero}

        recuperadas = ModelAddToUser.filter(db, id_user, filtro)
        generos = ModelGenero.Select(db,{})
        return render_template('index.html', recuperadas = recuperadas, generos = generos,autor = "", nombre = "", user = id_user, id_gen = id_gen)    
    else:
        return render_template('auth/login.html') """

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    # Lógica para la página de registro
    if request.method == 'POST':
        password_hashed = User.set_password(request.form['password'])
        user = User(0, request.form['name'], request.form['email'], password_hashed, request.form['username'])
        success = ModelUser.register(db, user)
        logged_user = ModelUser.login(db,user)
        ModelCrearTabla.CrearTablaUsurio(db, logged_user.id)

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
                return redirect(url_for('home', id_user = logged_user.id))
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
    return redirect(url_for('login'))

    

if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run()