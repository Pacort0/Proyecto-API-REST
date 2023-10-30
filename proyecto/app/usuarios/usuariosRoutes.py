from flask import *
from utils.funciones import leeFichero, escribeFichero
import bcrypt

usuariosBP = Blueprint('usuarios', __name__)
ficheroUsuarios = "../proyecto/datos_Editoriales/usuarios.json"

@usuariosBP.post('/')
def addUsuario():
    if request.is_json:
        usuarios = leeFichero(ficheroUsuarios)
        usuario = request.get_json()   
        password = usuario['password'].encode('utf-8')
        salt = bcrypt.gensalt()
        hashPassword = bcrypt.hashpw(password, salt).hex()
        usuario['password'] = hashPassword
        usuarios.append(usuario)  
        escribeFichero(ficheroUsuarios, usuarios)