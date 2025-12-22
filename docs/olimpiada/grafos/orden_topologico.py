grafo = {
    "A": ["C"],
    "B": ["C", "D"],
    "C": ["E"],
    "D": ["F"],
    "E": ["H", "F"],
    "F": ["G"],
    "G": [],
    "H": [],
}


def orden_topologico(grafo):
    visitado = set()
    pila = []

    def dfs(nodo):
        visitado.add(nodo)
        for vecino in grafo.get(nodo, []):
            if vecino not in visitado:
                dfs(vecino)
        pila.append(nodo)

    for nodo in grafo:
        if nodo not in visitado:
            dfs(nodo)

    return pila[::-1]  # Invierte la pila para obtener el orden topológico correcto


print(orden_topologico(grafo))
