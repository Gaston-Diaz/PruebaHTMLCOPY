import requests

def guardar_html(url, archivo):
    # Realizar la solicitud GET a la URL
    response = requests.get(url)
    
    # Comprobar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Guardar el contenido HTML en el archivo especificado
        with open(archivo, 'w', encoding='utf-8') as f:
            f.write(response.text)
        print(f'El HTML de {url} ha sido guardado en {archivo} exitosamente.')
    else:
        # Si la solicitud no fue exitosa, imprimir el código de estado
        print(f'Error al realizar la solicitud. Código de estado: {response.status_code}')

# URL del sitio web
url = 'http://10.1.8.82/web/guest/es/websys/status/getUnificationCounter.cgi'

# Nombre del archivo donde se guardará el HTML
archivo = 'html_output.html'

# Llamar a la función para guardar el HTML
guardar_html(url, archivo)
