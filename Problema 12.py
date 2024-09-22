tipos_mime = {
    '.gif': 'image/gif',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.png': 'image/png',
    '.pdf': 'application/pdf',
    '.txt': 'text/plain',
    '.zip': 'application/zip'
}

# Introducir el nombre del archivo
nombre_archivo = input("Introduce el nombre del archivo: ")


extension = '.' + nombre_archivo.split('.')[-1]

if extension in tipos_mime:
    tipo_mime = tipos_mime[extension]
else:
    tipo_mime = 'application/octet-stream'

# Mostrar resultados.
print(tipo_mime)