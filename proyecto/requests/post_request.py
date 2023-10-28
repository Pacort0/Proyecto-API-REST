import requests
api_url = "http://localhost:5050/editoriales"

todo = {"id":4, "CIF":"P76532498", "RazonSocial": "GRUPO KINKI SA", "Direccion":"C/Sergio Ramos, 69", "Web":"https://www.sergioramos.es/", "Correo":"grupokinki@gmail.com", "Telefono":617564329}
response = requests.post(api_url, json=todo)

print(response.json())

print("Código de estado:", response.status_code)