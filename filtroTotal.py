import re

# Función para filtrar y guardar el resultado de búsqueda en una variable
def extraer_numero_despues_de_palabra(ruta_archivo, palabra):
    # Variable para almacenar el número encontrado
    numero = None

    # Abrir el archivo en modo lectura
    with open(ruta_archivo, 'r') as archivo:
        # Leer cada línea del archivo
        for linea in archivo:
            # Buscar la palabra en la línea
            match = re.search(rf'{palabra}\s*:\s*(\d+)[a-zA-Z]*', linea)
            if match:
                numero = int(match.group(1))
                break  # Si encontramos el número, salimos del bucle

    # Devolver el número encontrado
    return numero

# Ruta del archivo de texto
ruta_archivo = 'elementos_filtrados.txt'

# Palabra clave
palabra = 'Total'

# Llamada a la función para extraer el número después de la palabra clave
numero_total = extraer_numero_despues_de_palabra(ruta_archivo, palabra)

# Imprimir el número encontrado
print("El número después de la palabra 'Total' es:", numero_total)
