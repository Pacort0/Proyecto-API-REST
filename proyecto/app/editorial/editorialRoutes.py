from utils.funciones import leeFichero, escribeFichero
from flask import *

#Creamos una variable en la que guardamos la ruta de fichero con los datos de las editoriales
ficheroEditoriales =  "proyecto/datos_Editoriales/editoriales.json"
#Creamos una variable en la que guardamos la ruta de fichero con los datos de los libros
ficheroLibros = "proyecto/datos_Editoriales/libros.json"

editorialesBP = Blueprint('editoriales', __name__)

#Creamos una función que nos ayude a asignar un valor 'id' automáticamente a las editoriales que creemos
def find_next_id():
    editoriales = leeFichero(ficheroEditoriales)#Leemos el fichero de editoriales y guardamos los datos en una variable
    max = editoriales[0]["id"]#Declaramos una variable max y le asignamos el primer id de la lista de editoriales
    for editorial in editoriales:#Iteramos en la lista de editoriales con un bucle for
        if editorial["id"] > max and editorial["id"] == max+1: #Si el id de la editorial actual es mayor que el id máximo guardado y es el valor consecutivo
            max = editorial["id"] #Cambiamos el valor de la variable 'max'
    return max+1 #Devolvemos el primer id libre que hayamos encontrado o el siguiente al último de la lista

@editorialesBP.get('/')  #Método HTTP para obtener las editorales de la base de datos
def getEditoriales():
    editoriales = leeFichero(ficheroEditoriales)#Leemos el fichero de editoriales y guardamos los datos en una variable
    return jsonify(editoriales) #Devolvemos una lista jsonificada de los editoriales

@editorialesBP.get("/<int:id>") #Método HTTP para obtener una editorial de la base de datos
def getEditorial(id):
    editoriales = leeFichero(ficheroEditoriales) #Leemos el fichero de editoriales y guardamos los datos en una variable
    for editorial in editoriales: #Iteramos en la lista de las editoriales con un bucle for
        if(editorial["id"] == id): #Si se encuentra una editorial cuyo id sea el mismo que el solicitado en la búsqueda
            return editorial, 200 #Devolvemos la editorial encontrada
    return{"error": "Editorial no encontrada"}, 404 #Si no se encuentra la editorial, mostramos el error pertinente

@editorialesBP.post('/') #Método HTTP para agregar una editorial
def addEditorial():
    editoriales = leeFichero(ficheroEditoriales) #Leemos el fichero de editoriales y guardamos los datos en una variable
    if request.is_json: #Si el request introducido es un json bien formado
        editorial  = request.get_json() #Creamos una variable para guardar la editorial a introducir
        editorial["id"] = find_next_id() #Le asignamos un id libre a la editorial
        editoriales.append(editorial) #Agregamos la editorial a la lista
        escribeFichero(ficheroEditoriales, editoriales) #Reescribimos el fichero con los nuevos cambios
        return editorial, 201 #Mostramos el libro introducido
    return {"error": "Request must be json"} #En caso de que el request no sea un json bien formado, mostramos el mensaje de error pertinente

@editorialesBP.put('/<int:id>')  #Método HTTP para editar todos los datos de una Editorial
@editorialesBP.patch('/<int:id>') #Método HTTP para editar uno o varios datos de una Editorial
def modifyEditorial(id):
    editoriales = leeFichero(ficheroEditoriales) #Leemos el fichero de editoriales y guardamos los datos en una variable
    newEditorial = request.get_json() #Creamos una variable para guardar los cambios que se desean realizar
    if request.is_json: #Si el request es un json bien formado 
        for editorial in editoriales: #Iteramos en la lista de editoriales mediante un bucle for
            if editorial["id"] == id: #Si se encuentra la editorial a editar
                for element in newEditorial: #Iteramos dentro de los cambios que se desean realizar
                    editorial[element] = newEditorial[element] #Cambiamos todos los campos que coincidan con los campos de la editorial
                escribeFichero(ficheroEditoriales, editoriales) #Reescribimos el fichero con los nuevos cambios
                return editorial, 200 #Devolvemos la editorial cambiada
            return {"error": "Editorial no encontrada"}, 404 #Si no se encuentra la editorial a editar, mostramos un mensaje de error
    return {"error": "Request must be json"}, 415 #Si el request no es un json bien formado, mostramos un mensaje de error

@editorialesBP.delete('/<int:id>') #Método HTTP para eliminar una editorial
def deleteEditorial(id):
    editoriales = leeFichero(ficheroEditoriales) #Leemos el fichero de editoriales y guardamos los datos en una variable
    for editorial in editoriales: #Iteramos dentro de la lista de editoriales
        if editorial["id"] == id: #Si se encuentra el id especificado en la URL
            editoriales.remove(editorial) #Eliminamos la editorial asignada a ese id
            escribeFichero(ficheroEditoriales, editoriales) #Reescribimos el fichero con los nuevos cambios
            return {}, 200 #Devolvemos un json vacío en señal de que se ha borrado con éxito
    return {"error": "Editorial no encontrada"}, 404 #Si no se encuentra la editorial, mostramos el mensaje de error correspondiente

@editorialesBP.get('/<int:id>/libros') #Método HTTP para obtener los libros de una editorial en concreto
def get_libros(id):
    list = [] #Lista vacía donde vamos a guardar los libros que encontremos
    libros = leeFichero(ficheroLibros)  #Leemos el fichero de libros y guardamos los datos en una variable)
    for libro in libros: #Iteramos en la lista de libros
        if libro["IdEditorial"] == id: #Si el IdEditorial del libro coincide con el id de la editorial que buscamos
            list.append(libro) #Añadimos a la lista de libros el libro encontrado
    if len(list) > 0: #Si la longitud de la lista al acabar la iteración es mayor que 0
        return list, 200 #Devolvemos la lista completada
    else:
        return {"error": "No hay libros para esta editorial"}, 404 #Si no, informamos al usuario de que no existen libros para esa Editorial


