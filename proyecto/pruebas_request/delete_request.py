import requests
api_url = "http://localhost:5050/editoriales/3"

response = requests.delete(api_url)

print("Código de estado:", response.status_code)

print(response.json())
