def generar_binarios(n, actual="", resultados=None):
    if resultados is None:
        resultados = []

    if len(actual) == n:
        resultados.append(actual)
        return

    # Llamada recursiva: Agrega '0' y '1' al string actual
    generar_binarios(n, actual + "0", resultados)
    generar_binarios(n, actual + "1", resultados)

    return resultados


print(generar_binarios(3))
