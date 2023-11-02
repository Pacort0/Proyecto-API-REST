from utils.funciones import leeFichero, escribeFichero
from flask import *
from flask_jwt_extended import jwt_required

#Creamos una variable en la que guardamos la ruta de fichero con los datos de los libros
ficheroLibros = "proyecto/datos_Editoriales/libros.json"

librosBP = Blueprint('libros', __name__)

#Creamos una función que nos ayude a asignar un valor 'id' automáticamente a los libros que creemos 
def find_next_id():
    libros = leeFichero(ficheroLibros) #Leemos el fichero de libros y guardamos los datos en una variable
    max = libros[0]["Id"] #Declaramos una variable max y le asignamos el primer id de la lista de libros
    for libro in libros: #Iteramos en la lista de libros con un bucle for
        if libro["Id"] == max+1: #Si el id del libro actual es mayor que el id máximo guardado y es el valor consecutivo
            max = libro["Id"] #Cambiamos el valor de la variable 'max'
    return max+1 #Devolvemos el primer id libre que hayamos encontrado o el siguiente al último de la lista

#Creamos una función que nos ayude a encontrar el primer hueco libre en la lista 
def find_next_spot():
    libros = leeFichero(ficheroLibros) #Leemos el fichero de libros y guardamos los datos en una variable
    hueco = 0 #Creamos una variable donde guardaremos el hueco libre que encontremos
    for libro in libros: #Iteramos en la lista de libros con un bucle for
        if libro["Id"] == hueco+1: #Si el id del libro es igual a la última posición+1
            hueco = libro["Id"] #Asignamos a la variable hueco el id de la editorial actual
    return hueco #Devolvemos la variable

@librosBP.get('/') #Método HTTP para obtener los libros de la base de datos
def getLibros(): 
    libros = leeFichero(ficheroLibros) #Leemos el fichero de libros y guardamos los datos en una variable
    return jsonify(libros) #Devolvemos una lista jsonificada de los libros

@librosBP.get("/<int:id>") #Método HTTP para obtener un libro de la base de datos
def getLibro(id):
    libros = leeFichero(ficheroLibros) #Leemos el fichero de libros y guardamos los datos en una variable
    for libro in libros: #Iteramos en la lista de libros con un bucle for
        if libro["Id"] == id: #Si el id del libro coincide con el id especificado en la búsqueda
            return libro, 200 #Devolvemos el libro encontrado
    return {"error":"Libro no encontrado"}, 404 #En caso de no encontrar el libro, mostramos el error correspondiente

@librosBP.post('/') #Método HTTP para crear un nuevo Libro
@jwt_required()
def addLibro():
    libros = leeFichero(ficheroLibros) #Leemos el fichero de libros y guardamos los datos en una variable
    if request.is_json: #Comprobamos que el request sea un json correctamente formado
        libro  = request.get_json() #Creamos una variable para guardar el libro que se quiere introducir
        position = find_next_spot()
        newId = find_next_id()
        libro["Id"] = newId #Asignamos una id al libro que deseamos introducir
        libros.insert(position, libro) #Añadimos el libro a la lista de libros
        escribeFichero(ficheroLibros, libros) #Reescribimos el fichero de libros con la nueva aportación
        return libro, 201 #Devolvemos el libro que se acaba de añadir
    return {"error": "Request must be json"}, 415 #Si el request no era un tipo json bien formado, mostramos el error correspondiente

@librosBP.put('/<int:id>') #Método HTTP para editar todos los datos de un Libro
@librosBP.patch('/<int:id>') #Método HTTP para editar uno o varios datos de un Libro
@jwt_required()
def modifyLibro(id):
    libros = leeFichero(ficheroLibros) #Leemos el fichero de libros y guardamos los datos en una variable
    newLibro = request.get_json() #Creamos una variable para guardar los cambios que se desean realizar
    if request.is_json: #Comprobamos que el request sea un json correctamente formado
        for libro in libros: #Iteramos en la lista de libros con un bucle for
            if libro["Id"] == id: #Si se encuentra un libro que encaje con el id pasado por parámetros
                for element in newLibro: #Iteramos dentro de los cambios a realizar en el Libro
                    libro[element] = newLibro[element] #Cambiamos todos los campos que coincidan con los campos del Libro
                escribeFichero(ficheroLibros, libros) #Reescribimos el fichero de libros con los cambios pertinentes
                return libro, 200 #Devolvemos el libro con sus datos cambiados
        return {"error": "Libro no encontrado"}, 404
    return {"error": "Request must be json"}, 415 #Si el request no era un tipo json bien formado, mostramos el error pertinente

@librosBP.delete('/<int:id>') #Método HTTP para borrar un Libro
@jwt_required()
def deleteLibro(id):
    libros = leeFichero(ficheroLibros) #Leemos el fichero de libros y guardamos los datos en una variable
    for libro in libros: #Iteramos en la lista de libros
        if libro["Id"] == id: #Si se encuentra el id especificado por parámetros
            libros.remove(libro) #Borramos el libro de la lista de libros
            escribeFichero(ficheroLibros, libros) #Reescribimos el fichero de libros con los cambios realizados
            return {}, 200 #Devolvemos un json en blanco
    return {"error": "Libro no encontrado"}, 404 #Si el libro introducido no se encuentra, se muestra el mensaje correspondiente
