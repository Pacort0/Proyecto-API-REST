import requests
api_url = "http://localhost:5050/editoriales"

todo = {"CIF":"F76532498", "RazonSocial": "GRUPO MARTA SA", "Direccion":"C/Jesús Navas, 69", "Web":"https://www.sergioramos.es/", "Correo":"grupomarta@gmail.com", "Telefono":617564329}
response = requests.post(api_url, json=todo)

print(response.json())

print("Código de estado:", response.status_code)