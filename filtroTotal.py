# Función para filtrar y guardar el resultado de búsqueda en una variable
def extraer_numero_despues_de_palabra(ruta_archivo, palabra, lineas_despues):
    # Variable para almacenar el número encontrado
    numero = None

    # Abrir el archivo en modo lectura
    with open(ruta_archivo, 'r') as archivo:
        # Bandera para indicar si se encontró la palabra
        encontrada = False

        # Leer cada línea del archivo
        for linea in archivo:
            # Buscar la palabra en la línea
            if palabra in linea:
                encontrada = True
                continue

            # Si ya se encontró la palabra, buscar el número en las siguientes líneas
            if encontrada:
                # Intentar convertir la línea en un número
                try:
                    numero = int(linea.strip())  # Eliminar espacios en blanco y convertir a entero
                    break  # Si se encuentra el número, salir del bucle
                except ValueError:
                    # Si no se puede convertir a un número, continuar buscando en la siguiente línea
                    continue

    # Devolver el número encontrado
    return numero

# Ruta del archivo de texto
ruta_archivo = 'elementos_filtrados.txt'

# Palabra clave
palabra = 'Total'

# Número de líneas después de la palabra para buscar el número
lineas_despues = 2

# Llamada a la función para extraer el número después de la palabra clave
numero_total = extraer_numero_despues_de_palabra(ruta_archivo, palabra, lineas_despues)

# Imprimir el número encontrado
print("El número después de la palabra 'Total' es:", numero_total)
