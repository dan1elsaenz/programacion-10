"""
Ejemplo de ejecución del módulo `os`
"""

import os

ruta_relativa = "archivo.txt"
ruta_absoluta = os.path.abspath(ruta_relativa)  # Devuelve la ruta absoluta
existe = os.path.exists(ruta_relativa)          # Verifica si el archivo existe
carpeta = os.path.dirname(ruta_absoluta)        # Extrae el directorio
nombre_archivo = os.path.basename(ruta_absoluta) # Extrae el nombre del archivo

print("Ruta absoluta:", ruta_absoluta)
print("¿Existe el archivo?", existe)
print("Carpeta contenedora:", carpeta)
print("Nombre del archivo:", nombre_archivo)

