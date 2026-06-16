"""
=============================================================================
PSEUDOCÓDIGO — Verificação de Grafo Euleriano
=============================================================================

função verificar_euleriano(arestas):
    1. Calcular grau de cada vértice:
       grau[v] ← 0 para todo v
       para cada aresta (u, v) em arestas:
           grau[u] ← grau[u] + 1
           grau[v] ← grau[v] + 1

    2. Verificar conectividade (ignorando vértices isolados):
       se grafo não é conexo:
           retornar "Nenhum"

    3. Contar vértices com grau ímpar:
       impares ← |{v : grau[v] é ímpar}|

    4. Classificar:
       se impares == 0:
           retornar "Euleriano"        ← circuito Euleriano existe
       se impares == 2:
           retornar "Semi-Euleriano"   ← trilha Euleriana existe
       caso contrário:
           retornar "Nenhum"

=============================================================================
"""

from collections import defaultdict, deque


def verificar_euleriano(arestas):
    """
    Verifica se um grafo não-dirigido é Euleriano, Semi-Euleriano ou Nenhum.

    Parâmetros:
        arestas: lista de tuplas (u, v) — grafo não-dirigido

    Retorna:
        classificacao: str — "Euleriano", "Semi-Euleriano" ou "Nenhum"
        graus: dicionário {vertice: grau}
    """
    # ── Passo 1: calcular grau de cada vértice ────────────────────────────────
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

    # ── Passo 2: verificar conectividade (BFS) ────────────────────────────────
    # Considera apenas vértices com grau > 0
    ativos = {v for v in vertices if grau[v] > 0}

    if not ativos:
        # Grafo sem arestas: trivialmente Euleriano (circuito vazio)
        return "Euleriano", dict(grau)

    inicio = next(iter(ativos))
    visitados = set()
    fila = deque([inicio])

    while fila:
        v = fila.popleft()
        if v in visitados:
            continue
        visitados.add(v)
        for viz in adj[v]:
            if viz not in visitados:
                fila.append(viz)

    if visitados != ativos:
        # Grafo desconexo (desconsiderando vértices isolados)
        return "Nenhum", dict(grau)

    # ── Passo 3: contar vértices com grau ímpar ───────────────────────────────
    impares = [v for v in vertices if grau[v] % 2 != 0]
    qtd_impares = len(impares)

    # ── Passo 4: classificar ──────────────────────────────────────────────────
    if qtd_impares == 0:
        classificacao = "Euleriano"
    elif qtd_impares == 2:
        classificacao = "Semi-Euleriano"
    else:
        classificacao = "Nenhum"

    return classificacao, dict(grau)


def exibir_resultado(arestas, nome="Grafo"):
    print(f"\n=== {nome} ===")
    print(f"Arestas: {arestas}")

    classificacao, graus = verificar_euleriano(arestas)

    print("Grau de cada vértice:")
    for v, g in sorted(graus.items()):
        paridade = "ímpar" if g % 2 != 0 else "par"
        print(f"  vértice {v}: grau {g} ({paridade})")

    impares = [v for v, g in graus.items() if g % 2 != 0]
    print(f"Vértices com grau ímpar: {sorted(impares)} ({len(impares)} no total)")
    print(f"Classificação: {classificacao}")


# ── Testes ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # Euleriano: ciclo K3 — todos os vértices com grau 2 (par), grafo conexo
    arestas_euleriano = [
        (0, 1), (1, 2), (2, 0)
    ]
    exibir_resultado(arestas_euleriano, "Euleriano (todos graus pares)")

    # Semi-Euleriano: caminho 0-1-2-3-0-2 → vértices 0 e 2 com grau ímpar
    arestas_semi = [
        (0, 1), (1, 2), (2, 3), (3, 0), (0, 2)
    ]
    exibir_resultado(arestas_semi, "Semi-Euleriano (2 vértices ímpares)")

    # Nenhum: estrela K1,3 — vértice central grau 3, folhas grau 1 (4 ímpares)
    arestas_nenhum = [
        (0, 1), (0, 2), (0, 3)
    ]
    exibir_resultado(arestas_nenhum, "Nenhum (4 vértices ímpares)")

    # Desconexo
    arestas_desconexo = [
        (0, 1), (1, 0),   # componente 1
        (2, 3), (3, 2),   # componente 2 — desconexo
    ]
    exibir_resultado(arestas_desconexo, "Nenhum (grafo desconexo)")
