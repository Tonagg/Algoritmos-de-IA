import heapq

def a_estrella(grafo, heuristicas, inicio, meta):
    # pq guarda: (f_costo, g_costo, nodo_actual, camino)
    pq = [(heuristicas[inicio], 0, inicio, [inicio])]
    visitados = {}

    while pq:
        f, g, nodo, camino = heapq.heappop(pq)

        if nodo == meta:
            return camino, g

        if nodo not in visitados or g < visitados[nodo]:
            visitados[nodo] = g

            for vecino, costo_arista in grafo.get(nodo, []):
                nuevo_g = g + costo_arista
                nuevo_f = nuevo_g + heuristicas.get(vecino, 0)
                heapq.heappush(pq, (nuevo_f, nuevo_g, vecino, camino + [vecino]))

    return None, float('inf')

# Datos: Grafo (pesos reales) y Heurísticas (estimaciones)
grafo = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 5)],
    'C': [('D', 1)],
    'D': []
}
h = {'A': 6, 'B': 4, 'C': 1, 'D': 0}

camino_optimo, costo_total = a_estrella(grafo, h, 'A', 'D')
print(f"Camino A*: {camino_optimo} | Costo Real: {costo_total}")