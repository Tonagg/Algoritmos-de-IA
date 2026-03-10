import heapq

def a_star(grafo, heuristica, inico, meta):
    # pq guarda:*(f_costo, g_costo, nodo_actual, camino)
    pq = [(heuristica[inico], 0, inico, [inico])]
    visitados = {}

    while pq:
        f, g, camino = heapq.heappop(pq)

        if nodo == meta:
            return camino, g

        if nodo not in visitados or g < visitados[nodo]:
            visitados[nodo] = g

            for vecino, costo_artista in grafo.get(nodo, []):
                nuevo_g = g + costo_artista
                nuevo_f = nuevo_g + heuristica.get(vecino,0)
                heapq.heappush(pq, (nuevo_f, nuevo_g, vecino, camino + [vecino]))

    return None, float('inf')            

# Datos: Grafo*(pesos reales )y heurística (estimación de costo a meta)
grafo = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 5)],
    'C': [('D', 1)],
    'D': []
}   
h={
    'A': 6,
    'B': 4,
    'C': 1,
    'D': 0
}
camino_optimo, costo_total = a_star(grafo, h, 'A', 'D')
print(f"Camino A*: {camino_optimo}, Costo total: {  costo_total}")  