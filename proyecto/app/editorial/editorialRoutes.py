from utils.funciones import leeFichero, escribeFichero
from flask import *

ficheroEditoriales =  "proyecto/datos_Editoriales/editoriales.json"
ficheroLibros = "proyecto/datos_Editoriales/libros.json"

editorialesBP = Blueprint('editoriales', __name__)

def find_next_id():
    editoriales = leeFichero(ficheroEditoriales)
    max = editoriales[0]["id"]
    for editorial in editoriales:
        if editorial["id"] > max:
            max = editorial["id"]
    return max+1

@editorialesBP.get('/')
def getEditoriales():
    editoriales = leeFichero(ficheroEditoriales)
    return jsonify(editoriales)

@editorialesBP.get("/<int:id>")
def getEditorial(id):
    editoriales = leeFichero(ficheroEditoriales)
    for editorial in editoriales:
        if(editorial["id"] == id):
            return editorial, 200
    return{"error": "Editorial no encontrada"}, 404

@editorialesBP.post('/')
def addEditorial():
    editoriales = leeFichero(ficheroEditoriales)
    if request.is_json:
        editorial  = request.get_json()
        editorial["id"] = find_next_id()
        editoriales.append(editorial)
        escribeFichero(ficheroEditoriales, editoriales)
        return editorial, 201
    return {"error": "Request must be json"}

@editorialesBP.put('/<int:id>')
@editorialesBP.patch('/<int:id>')
def modifyEditorial(id):
    editoriales = leeFichero(ficheroEditoriales)
    newEditorial = request.get_json
    if request.is_json:
        for editorial in editoriales:
            if editorial["id"] == id:
                for element in newEditorial:
                    editorial[element] = newEditorial[element]
                escribeFichero(ficheroEditoriales, editoriales)
                return editorial, 200
    return {"error": "Request must be json"}, 415

@editorialesBP.delete('/<int:id')
def deleteEditorial(id):
    editoriales = leeFichero(ficheroEditoriales) 
    for editorial in editoriales:
        if editorial["id"] == id:
            editoriales.remove(editorial[id])
            escribeFichero(ficheroEditoriales, editoriales)
            return {}, 200
    return {"error": "Editorial no encontrada"}, 404


