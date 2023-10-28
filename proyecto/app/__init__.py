from flask import Flask
from .editorial.editorialRoutes import editorialesBP

app = Flask(__name__)

app.register_blueprint(editorialesBP, url_prefix='/editoriales')