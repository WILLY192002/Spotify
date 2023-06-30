from models.ModelGenero import ModelGenero
from models.ModelUser import ModelUser

import os


def verificarGenero(db, filtro):
    Genero = ModelGenero.Select(db, filtro)
    if len(Genero) != 0:
        return Genero
    else:
        return False


def subirImagen(Autor, Nombre, rutaDestino, Archivo):
    nombre_archivo, Extension = os.path.splitext(Archivo.filename)
    if not os.path.exists(rutaDestino):
        # Crear la carpeta
        os.makedirs(rutaDestino)
        print('Carpeta creada con éxito')
    Archivo.save(os.path.join(rutaDestino, '{}-{}{}'.format(Autor.capitalize(), Nombre.capitalize(),Extension)))

def renombrarArchivo(rutaDestino, nuevonombre):
    if os.path.exists(rutaDestino):
        os.rename(rutaDestino,nuevonombre)

def borrarArchivo(ruta):
    if os.path.exists(ruta):
        os.remove(ruta)
        


def subirAudio(Autor, Nombre, rutaDestino, Archivo):
    if not os.path.exists(rutaDestino):
        # Crear la carpeta
        os.makedirs(rutaDestino)
        print('Carpeta creada con éxito')
    Archivo.save(os.path.join(rutaDestino, '{}-{}.mp3'.format(Autor.capitalize(), Nombre.capitalize())))


def verificarUsuario(db, id_user):
    Usuario = ModelUser.get_by_id(db, id_user)
    if len(Usuario) != 0:
        return Usuario
    else:
        return False