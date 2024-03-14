import re
import requests
from bs4 import BeautifulSoup

# URL de la página web de la que quieres obtener el HTML
#url = "http://10.1.8.82/web/guest/es/websys/status/getUnificationCounter.cgi"
url = "http://10.1.9.138/web/guest/es/websys/status/getUnificationCounter.cgi"

try:
    # Realizar la solicitud HTTP para obtener el contenido de la página
    response = requests.get(url)
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Obtener el contenido HTML de la respuesta
        html_content = response.text
    else:
        print("Error al obtener el contenido de la página. Código de estado:", response.status_code)
        exit()
except requests.RequestException as e:
    print("Error al realizar la solicitud HTTP:", e)
    exit()

# Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(html_content, "html.parser")

# Encontrar todas las tablas en el HTML
tablas = soup.find_all("table")

# Palabras específicas que quieres buscar en los elementos de la tabla
palabras_especificas = ["Total", "Copiadora", "Impresora", "Fax"]

# Utilizar expresiones regulares para buscar las palabras específicas
palabras_regex = re.compile('|'.join(palabras_especificas), re.IGNORECASE)

# Inicializar una lista para almacenar los elementos de las tablas que contienen las palabras específicas
elementos_filtrados = []

# Iterar sobre todas las tablas encontradas
for tabla in tablas:
    # Encontrar todos los elementos de la tabla
    elementos = tabla.find_all(["th", "td"])
    # Filtrar elementos que contienen palabras específicas
    for elemento in elementos:
        texto = elemento.get_text().strip()
        if palabras_regex.search(texto):
            elementos_filtrados.append(texto)

# Guardar los elementos filtrados en un archivo
with open("elementos_filtrados.txt", "w", encoding="utf-8") as output_file:
    for elemento in elementos_filtrados:
        output_file.write(elemento + "\n")
