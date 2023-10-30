from flask import Flask
from .editorial.editorialRoutes import editorialesBP
from .libros.librosRoutes import librosBP
from .usuarios.usuariosRoutes import usuariosBP
from flask_jwt_extended import JWTManager

#Creamos una varianle de tipo Flask
app = Flask(__name__)
app.config['Miguel_pelate'] = 'la clave'
jwt = JWTManager(app)

#Registramos los blueprints de las Editoriales y de los Libros
app.register_blueprint(editorialesBP, url_prefix='/editoriales')
app.register_blueprint(librosBP, url_prefix='/libros')
app.register_blueprint(usuariosBP, url_prefix='/usuarios')