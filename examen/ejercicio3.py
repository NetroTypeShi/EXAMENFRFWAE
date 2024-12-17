import requests
import re
# URL base del servidor local, con la ruta '/shared_data'
url = "http://192.168.60.211:8080/shared_data"

# Datos que enviaremos en la solicitud POST. Podemos enviar un parámetro cualquiera
# en el cuerpo (data) o como parte de la URL (query).
data = {'dummy_key': 'dummy_value'}  # Parámetro arbitrario en el body

# Realizamos la petición POST a la ruta '/shared_data', enviando los datos
response = requests.post(url, data=data)

# Verificamos si la solicitud fue exitosa
print(response.text)

