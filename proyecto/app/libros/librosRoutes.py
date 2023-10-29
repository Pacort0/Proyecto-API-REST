from utils.funciones import *
from flask import *

ficheroLibros = "proyecto/datos_Editoriales/libros.json"

librosBP = Blueprint('libros', __name__)

def find_next_id():
    libros = leeFichero(ficheroLibros)
    max = libros[0]["Id"]
    for libro in libros:
        if libro["Id"] > max:
            max = libro["Id"]
    return max+1

@librosBP.get('/')
def getLibros():
    libros = leeFichero(ficheroLibros)
    return jsonify(libros)

@librosBP.get("/<int:id>")
def getLibro(id):
    libros = leeFichero(ficheroLibros)
    for libro in libros:
        if libro["Id"] == id:
            return libro, 200
    return {"error":"Libro no encontrado"}, 404

@librosBP.post('/')
def addLibro():
    libros = leeFichero(ficheroLibros)
    if request.is_json:
        libro  = request.get_json()
        libro["Id"] = find_next_id()
        libros.append(libro)
        escribeFichero(ficheroLibros, libros)
        return libro, 201
    return {"error": "Request must be json"}

@librosBP.put('/<int:id>')
@librosBP.patch('/<int:id>')
def modifyLibro(id):
    libros = leeFichero(ficheroLibros)
    newLibro = request.get_json()
    if request.is_json:
        for libro in libros:
            if libro["Id"] == id:
                for element in newLibro:
                    libro[element] = newLibro[element]
                escribeFichero(ficheroLibros, libros)
                return libro, 200
    return {"error": "Request must be json"}, 415

@librosBP.delete('/<int:id>')
def deleteLibro(id):
    libros = leeFichero(ficheroLibros) 
    for libro in libros:
        if libro["Id"] == id:
            libros.remove(libro)
            escribeFichero(ficheroLibros, libros)
            return {}, 200
    return {"error": "Editorial no encontrada"}, 404
