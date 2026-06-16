# Questão 18 - Percurso em Profundidade (DFS) Recursivo e Iterativo

def dfs_recursivo(grafo, vertice, visitados=None):
    if visitados is None:
        visitados = set()

    visitados.add(vertice)
    print(vertice, end=" ")

    for vizinho in grafo.get(vertice, []):
        if vizinho not in visitados:
            dfs_recursivo(grafo, vizinho, visitados)

    return visitados


def dfs_iterativo(grafo, inicio):
    visitados = set()
    pilha = [inicio]

    while pilha:
        vertice = pilha.pop()

        if vertice in visitados:
            continue

        visitados.add(vertice)
        print(vertice, end=" ")

        for vizinho in grafo.get(vertice, []):
            if vizinho not in visitados:
                pilha.append(vizinho)

    return visitados


if __name__ == "__main__":
    grafo = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2]
    }

    print("DFS Recursivo a partir do vértice 0:")
    dfs_recursivo(grafo, 0)
    print()

    print("DFS Iterativo a partir do vértice 0:")
    dfs_iterativo(grafo, 0)
    print()
