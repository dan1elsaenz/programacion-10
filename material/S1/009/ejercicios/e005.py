"""
5. Historial de navegación web

Guarda en una lista de tuplas las visitas a sitios web en formato (usuario, sitio, fecha).
Luego:

Crea un diccionario con claves usuario y valores como sets de sitios visitados.
Muestra los sitios comunes entre todos los usuarios.
"""

# Lista inicial con la información
actividad_usuarios = [
  ("Ana", "wikipedia.org", "2024-05-01"),
  ("Ana", "openai.com", "2024-05-02"),
  ("Luis", "google.com", "2024-05-01"),
  ("Luis", "wikipedia.org", "2024-05-03")
]

# diccionario = {
#     "Ana": {"wikipedia.org", "openai.com"},
#     "Luis": {"wikipedia.org", "openai.com"}
# }

# Declarar diccionario
diccionario = dict()

# Recorrer lista de `actividad_usuarios` y agregar contenidos al diccionario
# Índice 0: el nombre del usuario
# Índice 1: la página visitada
for usuario, pagina, fecha in actividad_usuarios:
    # Verificar si no existe una clave con el usuario
    if usuario not in diccionario.keys():
        diccionario.update({ usuario : set() })

    # Agregar página al set en la clave `usuario` del diccionario
    diccionario[usuario].add(pagina)

# Imprimir los sitios por usuario
for usuario, conjunto in diccionario.items():
    print(f"\nUsuario: {usuario}")
    print(conjunto)

# Realizar intersección entre los sets de todos los usuarios
sitios_comunes = set.intersection(*diccionario.values())

print("\n--- Sitios comunes ---")
print(sitios_comunes)
