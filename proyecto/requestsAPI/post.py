import requests

url = "http://localhost:5050/editoriales"

dict={"usuario":"pakito", "password":"1234"}

header = {"Authorization":"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5OTg2ODI0OSwianRpIjoiMGU2MTdkOTktZDI3Mi00NjRiLTgyNWQtMGM3OGU0OGQ0YTMyIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6InBha2l0byIsIm5iZiI6MTY5OTg2ODI0OSwiZXhwIjoxNjk5ODY5MTQ5fQ.5PfjxglqeU40TrRN5TXiMeLu9FuCpaTIavqUdCx5FDA"}
response = requests.post(url, headers=header, json=dict)
print (response.json())
print (response.status_code)
