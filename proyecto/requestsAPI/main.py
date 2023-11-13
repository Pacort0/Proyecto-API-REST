import requests 


def getEditorial():
    editorial = int(input(("Introduzca una editorial: ")))

    url = "http://localhost:5050/editoriales/" + str(editorial)
    response = requests.get(url)
    print (response.json())    
    print (response.status_code)

def getAllEditoriales():
    url = "http://localhost:5050/editoriales"

    response = requests.get(url)
    print (response.json())
    print (response.status_code)