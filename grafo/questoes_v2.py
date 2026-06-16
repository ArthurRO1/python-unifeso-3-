# Questão 18 - Percurso em Profundidade (DFS) Recursivo e Iterativo

def dfs_recursivo(grafo, vertice, visitados=None):
    if visitados is None:
        visitados = set()

    if vertice in visitados:
        return visitados

    visitados.add(vertice)
    print(vertice, end=" ")

    for vizinho in grafo.get(vertice, []):
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


# -------------------------------------------------------
# Questão 19 - Percurso em Largura (BFS) e verificação de caminho entre dois vértices

from collections import deque


def bfs(grafo, inicio):
    visitados = set([inicio])
    fila = deque([inicio])

    print(f"BFS a partir do vértice {inicio}: ", end="")

    while fila:
        vertice = fila.popleft()
        print(vertice, end=" ")

        for vizinho in grafo.get(vertice, []):
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    print()
    return visitados


def existe_caminho(grafo, origem, destino):
    if origem == destino:
        return True

    visitados = set([origem])
    fila = deque([origem])

    while fila:
        for vizinho in grafo.get(fila.popleft(), []):
            if vizinho == destino:
                return True
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

    return False


if __name__ == "__main__":
    grafo = {
        0: [1, 2],
        1: [0, 3, 4],
        2: [0, 5],
        3: [1],
        4: [1],
        5: [2]
    }

    bfs(grafo, 0)

    print(f"Existe caminho entre 0 e 5? {existe_caminho(grafo, 0, 5)}")
    print(f"Existe caminho entre 3 e 5? {existe_caminho(grafo, 3, 5)}")

    grafo_desconectado = {
        0: [1],
        1: [0],
        2: [3],
        3: [2]
    }

    print(f"\nExiste caminho entre 0 e 3? {existe_caminho(grafo_desconectado, 0, 3)}")
    print(f"Existe caminho entre 0 e 1? {existe_caminho(grafo_desconectado, 0, 1)}")


# -------------------------------------------------------
# Questão 20 - Lista de Adjacências, Matriz de Adjacências e conversão entre elas


def criar_lista_adjacencias(num_vertices, arestas, direcionado=False):
    lista = {i: [] for i in range(num_vertices)}

    for u, v in arestas:
        lista[u].append(v)
        if not direcionado:
            lista[v].append(u)

    return lista


def criar_matriz_adjacencias(num_vertices, arestas, direcionado=False):
    matriz = [[0] * num_vertices for _ in range(num_vertices)]

    for u, v in arestas:
        matriz[u][v] = 1
        if not direcionado:
            matriz[v][u] = 1

    return matriz


def lista_para_matriz(lista):
    n = len(lista)
    matriz = [[0] * n for _ in range(n)]

    for vertice, vizinhos in lista.items():
        for vizinho in vizinhos:
            matriz[vertice][vizinho] = 1

    return matriz


def imprimir_lista(lista):
    print("Lista de Adjacências:")
    for vertice, vizinhos in lista.items():
        print(f"  {vertice} -> {vizinhos}")


def imprimir_matriz(matriz):
    print("Matriz de Adjacências:")
    n = len(matriz)
    print("   " + " ".join(str(j) for j in range(n)))
    for i, linha in enumerate(matriz):
        print(f"  {i} {linha}")


if __name__ == "__main__":
    arestas = [(0, 1), (0, 2), (1, 3), (1, 4), (2, 5)]
    num_vertices = 6

    lista = criar_lista_adjacencias(num_vertices, arestas)
    matriz = criar_matriz_adjacencias(num_vertices, arestas)

    imprimir_lista(lista)
    print()
    imprimir_matriz(matriz)

    print("\nMatriz convertida a partir da Lista de Adjacências:")
    matriz_convertida = lista_para_matriz(lista)
    imprimir_matriz(matriz_convertida)

    print(f"\nAs matrizes são iguais? {matriz == matriz_convertida}")
