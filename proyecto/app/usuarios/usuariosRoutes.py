from flask import *
from utils.funciones import leeFichero, escribeFichero
from flask_jwt_extended import *
import bcrypt

usuariosBP = Blueprint('usuarios', __name__)
ficheroUsuarios = "proyecto/datos_Editoriales/usuarios.json"

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
        token = create_access_token(identity=usuario["usuario"])
        return {'token': token}, 201
    return{"error":"Request must be json"}

@usuariosBP.get('/')
def loginUser():
    usuarios = leeFichero(ficheroUsuarios)
    if request.is_json:
        usuario = request.get_json()
        nombreUsuario = usuario['usuario']
        password = usuario['password'].encode('utf-8')
        for userFile in usuarios:
            if userFile['usuario'] == nombreUsuario:
                passwordFile = userFile['password']
                if bcrypt.checkpw(password, bytes.fromhex(passwordFile)):
                    token = create_access_token(identity=nombreUsuario)
                    return{'token':token}, 200
                else:
                    return{'error': 'La contraseña es errónea'}, 401
        return {'error':'Usuario no encontrado'}, 404
    return{'error':'Request must be JSON'},415  
