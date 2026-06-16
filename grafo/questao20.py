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
    num_vertices = len(lista)
    matriz = [[0] * num_vertices for _ in range(num_vertices)]

    for vertice, vizinhos in lista.items():
        for vizinho in vizinhos:
            matriz[vertice][vizinho] = 1

    return matriz


def imprimir_lista(lista):
    print("Lista de Adjacências:")
    for vertice, vizinhos in lista.items():
        print(f"  {vertice}: {vizinhos}")


def imprimir_matriz(matriz):
    print("Matriz de Adjacências:")
    n = len(matriz)
    print("    " + "  ".join(str(j) for j in range(n)))
    for i, linha in enumerate(matriz):
        print(f"  {i} [{', '.join(str(v) for v in linha)}]")


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
