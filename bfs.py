def bfs(grafo, inicio):
    # Conjunto para rastrear nodos visitados
    visitados = set()
    # Cola para manejar el orden de exploración (FIFO)
    cola = deque([inicio])

    # Marcamos el inicio como visitado
    visitados.add(inicio)

    print(f"Orden de exploración empezando desde {inicio}:")

    while cola:
        # Extraemos el nodo que llegó primero
        nodo_actual = cola.popleft()
        print(nodo_actual, end=" ")

        # Revisamos los vecinos del nodo actual
        for vecino in grafo[nodo_actual]:
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append(vecino)
