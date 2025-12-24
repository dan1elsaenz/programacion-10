
def tiene_ciclo(grafo):
    visitado = set()

    def dfs(nodo, padre):
        visitado.add(nodo)
        for vecino in grafo[nodo]:
            if vecino not in visitado:
                if dfs(vecino, nodo):
                    return True
            elif vecino != padre:
                return True
        return False

    for nodo in grafo:
        if nodo not in visitado:
            if dfs(nodo, None):
                return True
    return False
