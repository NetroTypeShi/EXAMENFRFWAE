import requests
import re

url = "http://192.168.60.211:8080/shared_data?dummy_key=dummy_value"  # Parámetro en la URL

# Realizamos la petición POST a la ruta '/shared_data' (aunque los datos van en la URL)
response = requests.post(url)

# Verificamos si la solicitud fue exitosa
print(response.text)

   
