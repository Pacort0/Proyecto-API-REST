from flask import Flask
from .editorial.editorialRoutes import editorialesBP
from .libros.librosRoutes import librosBP

app = Flask(__name__)

app.register_blueprint(editorialesBP, url_prefix='/editoriales')
app.register_blueprint(librosBP, url_prefix='/libros')