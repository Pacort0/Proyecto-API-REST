from flask import Flask
from .editorial.editorialRoutes import editorialesBP
from .libros.librosRoutes import librosBP

#Creamos una varianle de tipo Flask
app = Flask(__name__)

#Registramos los blueprints de las Editoriales y de los Libros
app.register_blueprint(editorialesBP, url_prefix='/editoriales')
app.register_blueprint(librosBP, url_prefix='/libros')