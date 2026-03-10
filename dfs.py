def dfs(grafo, nodo, visitados=None):
    if visitados is None:
        visitados = set()

    # Marcamos el nodo como visitado y lo procesamos
    visitados.add(nodo)
    print(nodo, end=" ")

    # Exploramos recursivamente cada vecino
    for vecino in grafo[nodo]:
        if vecino not in visitados:
            dfs(grafo, vecino, visitados)

# Grafo de ejemplo
grafo_ejemplo = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}

print("Orden de exploración DFS empezando desde 2:")
dfs(grafo_ejemplo, 2)