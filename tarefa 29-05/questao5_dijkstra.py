import heapq
from collections import defaultdict

def dijkstra_todos_caminhos(arestas, num_vertices, origem):
    """
    Dijkstra com grafo como lista de arestas.
    Retorna todos os caminhos mínimos para cada vértice de destino.

    Parâmetros:
        arestas: lista de tuplas (u, v, peso)
        num_vertices: número de vértices (0-indexado)
        origem: vértice de origem

    Retorna:
        dist: dicionário {vertice: distancia_minima}
        todos_caminhos: dicionário {vertice: [lista de caminhos mínimos]}
    """
    # Constrói lista de adjacência a partir da lista de arestas
    adj = defaultdict(list)
    for u, v, peso in arestas:
        adj[u].append((v, peso))
        adj[v].append((u, peso))  # remova esta linha se o grafo for dirigido

    dist = {i: float('inf') for i in range(num_vertices)}
    dist[origem] = 0

    # predecessores[v] = lista de vértices que levam a v com custo mínimo
    predecessores = defaultdict(list)

    heap = [(0, origem)]

    while heap:
        custo_atual, u = heapq.heappop(heap)

        if custo_atual > dist[u]:
            continue

        for v, peso in adj[u]:
            novo_custo = dist[u] + peso

            if novo_custo < dist[v]:
                dist[v] = novo_custo
                predecessores[v] = [u]
                heapq.heappush(heap, (novo_custo, v))

            elif novo_custo == dist[v]:
                # Outro caminho com mesmo custo mínimo
                predecessores[v].append(u)

    # Reconstrói todos os caminhos mínimos via backtracking
    def reconstruir(destino):
        if destino == origem:
            return [[origem]]
        if not predecessores[destino]:
            return []  # inalcançável
        caminhos = []
        for pred in predecessores[destino]:
            for caminho in reconstruir(pred):
                caminhos.append(caminho + [destino])
        return caminhos

    todos_caminhos = {}
    for v in range(num_vertices):
        todos_caminhos[v] = reconstruir(v)

    return dist, todos_caminhos


# ── Teste ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Grafo com 5 vértices (0-4)
    arestas = [
        (0, 1, 4),
        (0, 2, 1),
        (2, 1, 2),
        (1, 3, 1),
        (2, 3, 5),
        (3, 4, 3),
    ]

    origem = 0
    dist, caminhos = dijkstra_todos_caminhos(arestas, 5, origem)

    print(f"=== Dijkstra — origem: {origem} ===")
    for v in range(5):
        print(f"\nDestino {v} | distância mínima: {dist[v]}")
        for c in caminhos[v]:
            print(f"  caminho: {' -> '.join(map(str, c))}")
