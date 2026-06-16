# Questão 19 - Percurso em Largura (BFS) e verificação de caminho entre dois vértices

from collections import deque


def bfs(grafo, inicio):
    visitados = [inicio]
    fila = deque([inicio])

    print(f"BFS a partir do vértice {inicio}: ", end="")

    while fila:
        vertice = fila.popleft()
        print(vertice, end=" ")

        for vizinho in grafo.get(vertice, []):
            if vizinho not in visitados:
                visitados.append(vizinho)
                fila.append(vizinho)

    print()
    return visitados


def existe_caminho(grafo, origem, destino):
    if origem == destino:
        return True

    visitados = {origem}
    fila = deque([origem])

    while fila:
        vertice = fila.popleft()

        for vizinho in grafo.get(vertice, []):
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

    print(f"\nExiste caminho entre 0 e 3 (grafo desconectado)? {existe_caminho(grafo_desconectado, 0, 3)}")
    print(f"Existe caminho entre 0 e 1 (grafo desconectado)? {existe_caminho(grafo_desconectado, 0, 1)}")
