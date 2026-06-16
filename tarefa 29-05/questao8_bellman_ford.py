from collections import defaultdict, deque

def bellman_ford(adj, origem):
    """
    Bellman-Ford com grafo como dicionário de adjacências.
    Retorna distâncias e o conjunto de vértices afetados por ciclos negativos.

    Parâmetros:
        adj: dicionário {u: [(v, peso), ...]}
        origem: vértice de origem

    Retorna:
        dist: dicionário {vertice: distancia} (float('-inf') se afetado por ciclo negativo)
        afetados: conjunto de vértices alcançáveis a partir de um ciclo negativo
    """
    vertices = set(adj.keys())
    for vizinhos in adj.values():
        for v, _ in vizinhos:
            vertices.add(v)

    dist = {v: float('inf') for v in vertices}
    dist[origem] = 0

    n = len(vertices)

    # Relaxa todas as arestas n-1 vezes
    for _ in range(n - 1):
        atualizado = False
        for u in adj:
            if dist[u] == float('inf'):
                continue
            for v, peso in adj[u]:
                if dist[u] + peso < dist[v]:
                    dist[v] = dist[u] + peso
                    atualizado = True
        if not atualizado:
            break  # convergiu antes

    # Detecta ciclos negativos: vértices que ainda podem ser relaxados
    em_ciclo_negativo = set()
    for u in adj:
        if dist[u] == float('inf'):
            continue
        for v, peso in adj[u]:
            if dist[u] + peso < dist[v]:
                em_ciclo_negativo.add(v)

    # Propaga: todos os vértices alcançáveis a partir de um ciclo negativo
    # também são afetados (distância efetivamente -inf)
    afetados = set(em_ciclo_negativo)
    fila = deque(em_ciclo_negativo)

    while fila:
        u = fila.popleft()
        for v, _ in adj.get(u, []):
            if v not in afetados:
                afetados.add(v)
                fila.append(v)

    # Marca distâncias afetadas como -inf
    for v in afetados:
        dist[v] = float('-inf')

    return dist, afetados


# ── Teste ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Grafo dirigido com ciclo negativo entre 1-2-3
    adj = defaultdict(list, {
        0: [(1, 1)],
        1: [(2, 3)],
        2: [(3, -6)],
        3: [(1, 2)],   # ciclo negativo: 1->2->3->1 com peso 3-6+2 = -1
        3: [(4, 1)],
    })
    # Corrigindo: vértice 3 tem dois destinos
    adj = {
        0: [(1, 1)],
        1: [(2, 3)],
        2: [(3, -6)],
        3: [(1, 2), (4, 1)],  # ciclo negativo e saída para 4
        4: [],
    }

    origem = 0
    dist, afetados = bellman_ford(adj, origem)

    print("=== Bellman-Ford ===")
    print(f"Origem: {origem}")
    print("\nDistâncias:")
    for v, d in sorted(dist.items()):
        print(f"  vértice {v}: {d}")

    print(f"\nVértices afetados por ciclos negativos: {sorted(afetados)}")
