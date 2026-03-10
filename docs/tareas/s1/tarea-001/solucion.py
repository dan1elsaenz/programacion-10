candidatos = ["Valeria", "Andrés", "Camila", "Diego", "Fernanda"]
votos = [45, 38, 52, 29, 41]

print("=== Sistema de Votación Estudiantil ===")
print("1. Consultar votos de un candidato")
print("2. Registrar votos a un candidato")
print("3. Ver estadísticas generales")
print("4. Ver candidato ganador")

opcion = input("\nElija una opción: ").strip()

if opcion == "1":
    nombre = input("Digite el nombre del candidato: ").strip().title()

    if nombre in candidatos:
        indice = candidatos.index(nombre)
        votos_candidato = votos[indice]

        if votos_candidato >= 50:
            clasificacion = "Candidato destacado"
        elif votos_candidato >= 35:
            clasificacion = "Candidato competitivo"
        else:
            clasificacion = "Candidato con pocos votos"

        print(f"\nCandidato: {nombre}")
        print(f"Votos: {votos_candidato}")
        print(f"Clasificación: {clasificacion}")
    else:
        print(f"\nEl candidato '{nombre}' no está registrado.")

elif opcion == "2":
    nombre = input("Digite el nombre del candidato: ").strip().title()

    if nombre in candidatos:
        try:
            nuevos_votos = int(input("Digite la cantidad de votos a agregar: "))

            if nuevos_votos <= 0:
                print("Error: la cantidad de votos debe ser mayor a cero.")
            else:
                indice = candidatos.index(nombre)
                votos[indice] += nuevos_votos
                print(f"\nVotos registrados correctamente.")
                print(f"{nombre} ahora tiene {votos[indice]} votos.")

        except ValueError:
            print("Error: debe ingresar un número entero válido.")
    else:
        print(f"\nEl candidato '{nombre}' no está registrado.")

elif opcion == "3":
    total = sum(votos)
    promedio = total / len(votos)
    indice_max = votos.index(max(votos))
    indice_min = votos.index(min(votos))

    print("\n--- Estadísticas generales ---")
    print(f"Total de votos: {total}")
    print(f"Promedio por candidato: {promedio:.1f}")
    print(f"Candidato con más votos: {candidatos[indice_max]} ({votos[indice_max]})")
    print(f"Candidato con menos votos: {candidatos[indice_min]} ({votos[indice_min]})")

elif opcion == "4":
    max_votos = max(votos)
    ganadores = []

    for i in range(len(candidatos)):
        if votos[i] == max_votos:
            ganadores.append(candidatos[i])

    if len(ganadores) == 1:
        print(f"\nEl candidato ganador es: {ganadores[0]} con {max_votos} votos.")
    else:
        print(f"\nHay empate con {max_votos} votos entre:")
        for ganador in ganadores:
            print(f"  - {ganador}")

else:
    print("\nOpción inválida. Debe digitar un número del 1 al 4.")
