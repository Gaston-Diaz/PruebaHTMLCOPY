from bs4 import BeautifulSoup

# Leer el contenido del archivo HTML
with open("html_output.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Crear un objeto BeautifulSoup para analizar el HTML
soup = BeautifulSoup(html_content, "html.parser")

# Encontrar todas las tablas en el HTML
tablas = soup.find_all("table")

# Palabras específicas que quieres buscar en los elementos de la tabla
palabras_especificas = ["Total", "Copiadora", "Impresora", "Fax"]

# Inicializar una lista para almacenar los elementos de las tablas que contienen las palabras específicas
elementos_filtrados = []

# Iterar sobre todas las tablas encontradas
for tabla in tablas:
    # Encontrar todos los elementos de la tabla
    elementos = tabla.find_all(["th", "td"])
    # Iterar sobre los elementos de la tabla
    for elemento in elementos:
        # Verificar si el texto del elemento contiene alguna de las palabras específicas
        for palabra in palabras_especificas:
            if palabra in elemento.get_text():
                # Agregar el elemento a la lista de elementos filtrados
                elementos_filtrados.append(elemento)
                break  # Salir del bucle para evitar agregar el mismo elemento varias veces

# Guardar los elementos filtrados en un archivo
with open("elementos_filtrados.txt", "w", encoding="utf-8") as output_file:
    for elemento in elementos_filtrados:
        output_file.write(elemento.get_text() + "\n")
