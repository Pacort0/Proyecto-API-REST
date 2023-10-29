#Importamos la variable de tipo app
from app import app

#Damos las intrucciones al sistema para que use un servidor local cuando se ejecute el programa
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)