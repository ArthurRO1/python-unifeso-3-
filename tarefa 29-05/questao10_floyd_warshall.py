def floyd_warshall(n, arestas):
    """
    Floyd-Warshall com matriz de próximos vértices (next-hop).
    Detecta ciclos negativos pela diagonal.
    Reconstrói caminhos de forma iterativa (sem recursão).

    Parâmetros:
        n: número de vértices (0-indexado)
        arestas: lista de tuplas (u, v, peso)

    Retorna:
        dist: matriz n×n de distâncias mínimas
        prox: matriz n×n de próximos vértices para reconstrução
        ciclos_negativos: conjunto de vértices em ciclo negativo
    """
    INF = float('inf')

    # Inicialização
    dist = [[INF] * n for _ in range(n)]
    prox = [[None] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, peso in arestas:
        if peso < dist[u][v]:          # mantém a aresta de menor peso se houver paralelas
            dist[u][v] = peso
            prox[u][v] = v

    # Relaxamento principal
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
                        prox[i][j] = prox[i][k]

    # Detecção de ciclos negativos: dist[i][i] < 0
    ciclos_negativos = set()
    for i in range(n):
        if dist[i][i] < 0:
            ciclos_negativos.add(i)

    return dist, prox, ciclos_negativos


def reconstruir_caminho(prox, u, v):
    """
    Reconstrói o caminho de u até v de forma ITERATIVA usando a matriz prox.
    Retorna None se não houver caminho ou se passar por ciclo negativo.
    """
    if prox[u][v] is None:
        return None  # sem caminho

    caminho = [u]
    visitados = {u}

    while u != v:
        u = prox[u][v]
        if u is None:
            return None  # caminho interrompido
        if u in visitados:
            return None  # ciclo detectado durante reconstrução
        caminho.append(u)
        visitados.add(u)

    return caminho


# ── Teste ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("=== Teste 1: grafo sem ciclos negativos ===")
    n = 4
    arestas = [
        (0, 1, 3),
        (0, 2, 6),
        (1, 2, 1),
        (1, 3, 4),
        (2, 3, 2),
    ]

    dist, prox, ciclos = floyd_warshall(n, arestas)

    print("Matriz de distâncias:")
    for linha in dist:
        print("  ", ["inf" if x == float('inf') else x for x in linha])

    print("\nCaminhos mínimos:")
    for i in range(n):
        for j in range(n):
            if i != j:
                c = reconstruir_caminho(prox, i, j)
                caminho_str = " -> ".join(map(str, c)) if c else "sem caminho"
                print(f"  {i} -> {j}: {caminho_str}  (dist={dist[i][j]})")

    print(f"\nCiclos negativos detectados: {ciclos if ciclos else 'nenhum'}")

    print("\n=== Teste 2: grafo COM ciclo negativo ===")
    n2 = 3
    arestas2 = [
        (0, 1, 1),
        (1, 2, -3),
        (2, 1, 1),   # ciclo 1->2->1 com peso -3+1 = -2
    ]

    dist2, prox2, ciclos2 = floyd_warshall(n2, arestas2)

    print("Diagonal da matriz de distâncias:")
    for i in range(n2):
        print(f"  dist[{i}][{i}] = {dist2[i][i]}")

    print(f"\nCiclos negativos detectados (vértices): {sorted(ciclos2)}")
