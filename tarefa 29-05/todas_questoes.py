import heapq
from collections import defaultdict


# =============================================================================
# QUESTÃO 5 — Dijkstra com lista de arestas e todos os caminhos mínimos
# =============================================================================

def dijkstra_todos_caminhos(arestas, num_vertices, origem):
    adj = defaultdict(list)
    for u, v, peso in arestas:
        adj[u].append((v, peso))
        adj[v].append((u, peso))

    dist = [float('inf')] * num_vertices
    dist[origem] = 0
    anteriores = defaultdict(list)
    visitados = set()
    heap = [(0, origem)]

    while heap:
        custo, u = heapq.heappop(heap)
        if u in visitados:
            continue
        visitados.add(u)
        for v, peso in adj[u]:
            nova_dist = custo + peso
            if nova_dist < dist[v]:
                dist[v] = nova_dist
                anteriores[v] = [u]
                heapq.heappush(heap, (nova_dist, v))
            elif nova_dist == dist[v] and u not in anteriores[v]:
                anteriores[v].append(u)

    def montar_caminhos(no):
        if no == origem:
            return [[origem]]
        resultado = []
        for ant in anteriores[no]:
            for caminho in montar_caminhos(ant):
                resultado.append(caminho + [no])
        return resultado

    caminhos = {v: montar_caminhos(v) for v in range(num_vertices)}
    return dist, caminhos


# =============================================================================
# QUESTÃO 8 — Bellman-Ford com dicionário de adjacências
# =============================================================================

def bellman_ford(adj, origem):
    vertices = set(adj.keys())
    for vizinhos in adj.values():
        for v, _ in vizinhos:
            vertices.add(v)

    arestas = [(u, v, p) for u, vizinhos in adj.items() for v, p in vizinhos]

    dist = {v: float('inf') for v in vertices}
    dist[origem] = 0

    for _ in range(len(vertices) - 1):
        houve_mudanca = False
        for u, v, peso in arestas:
            if dist[u] != float('inf') and dist[u] + peso < dist[v]:
                dist[v] = dist[u] + peso
                houve_mudanca = True
        if not houve_mudanca:
            break

    em_ciclo = set()
    for u, v, peso in arestas:
        if dist[u] != float('inf') and dist[u] + peso < dist[v]:
            em_ciclo.add(v)

    afetados = set(em_ciclo)
    pilha = list(em_ciclo)
    while pilha:
        u = pilha.pop()
        for v, _ in adj.get(u, []):
            if v not in afetados:
                afetados.add(v)
                pilha.append(v)

    for v in afetados:
        dist[v] = float('-inf')

    return dist, afetados


# =============================================================================
# QUESTÃO 10 — Floyd-Warshall com matriz de próximos vértices
# =============================================================================

def floyd_warshall(n, arestas):
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]
    prox = [[None] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
        prox[i][i] = i

    for u, v, peso in arestas:
        if peso < dist[u][v]:
            dist[u][v] = peso
            prox[u][v] = v

    for k in range(n):
        for i in range(n):
            if dist[i][k] == INF:
                continue
            for j in range(n):
                nova = dist[i][k] + dist[k][j]
                if nova < dist[i][j]:
                    dist[i][j] = nova
                    prox[i][j] = prox[i][k]

    ciclos_negativos = {i for i in range(n) if dist[i][i] < 0}
    return dist, prox, ciclos_negativos


def reconstruir_caminho_fw(prox, origem, destino):
    if prox[origem][destino] is None:
        return None
    caminho = [origem]
    visitados = {origem}
    atual = origem
    while atual != destino:
        atual = prox[atual][destino]
        if atual is None or atual in visitados:
            return None
        caminho.append(atual)
        visitados.add(atual)
    return caminho


# =============================================================================
# QUESTÃO 15 — Verificação de Grafo Euleriano
# Pseudocódigo: calcular graus → verificar conectividade (DFS) →
#   0 ímpares = Euleriano | 2 ímpares = Semi-Euleriano | resto = Nenhum
# =============================================================================

def verificar_euleriano(arestas):
    grau = defaultdict(int)
    adj = defaultdict(set)

    for u, v in arestas:
        grau[u] += 1
        grau[v] += 1
        adj[u].add(v)
        adj[v].add(u)

    vertices = set(grau.keys())
    if not vertices:
        return "Nenhum", {}

    ativos = {v for v in vertices if grau[v] > 0}
    if not ativos:
        return "Euleriano", dict(grau)

    visitados = set()
    pilha = [next(iter(ativos))]
    while pilha:
        v = pilha.pop()
        if v in visitados:
            continue
        visitados.add(v)
        for viz in adj[v]:
            if viz not in visitados:
                pilha.append(viz)

    if visitados != ativos:
        return "Nenhum", dict(grau)

    qtd_impares = sum(1 for v in vertices if grau[v] % 2 != 0)

    if qtd_impares == 0:
        return "Euleriano", dict(grau)
    elif qtd_impares == 2:
        return "Semi-Euleriano", dict(grau)
    else:
        return "Nenhum", dict(grau)
