#fichero de funciones de ficheros

import json

#Función que lee los datos de un fichero y los carga en una variable
#Recibe por parámetros la ruta de un archivo
def leeFichero(nombreArchivo):
    archivo = open(nombreArchivo, "r") #Abre el archivo en modo Read, guardándolo en una variable
    data = json.load(archivo) #Cargamos en una variable los datos del archivo leído
    archivo.close() #Cerramos el archivo
    return data #Devolvemos los datos leídos

#Función que escribe datos en un archivo
#Recibe por parámetros la ruta de un archivo y los datos a escribir en él
def escribeFichero(nombreArchivo, datos):
    archivo = open(nombreArchivo, "w") #Abre el archivo en modo Write, guardándolo en una variable
    json.dump(datos, archivo) #Escribe en el archivo los datos correspondientes
    archivo.close() #Cierra el archivo