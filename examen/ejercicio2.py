import requests
import re

# URL base del servidor local, con la ruta '/metodo'
url = "http://192.168.60.211:8080/metodo/"  # Ruta modificada según la nueva indicación


# Realizamos una petición GET a la ruta '/metodo'
response = requests.get(url)
data = requests.post(url)
response2 = requests.patch(url)


# Verificamos si la solicitud fue exitosa
print (response.text)
print (data.text)
print (response2.text)