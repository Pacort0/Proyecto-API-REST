import json

def leeFichero(nombreArchivo):
    archivo = open(nombreArchivo, "r")
    data = json.load(archivo)
    archivo.close()
    return data

def escribeFichero(nombreArchivo, datos):
    archivo = open(nombreArchivo, "w")
    json.dump(datos, archivo)
    archivo.close()