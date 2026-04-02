import random
import time

def busca_sequencial(lista, alvo):
    for i in range(len(lista)):
        if lista[i] == alvo:
            return i
    return -1


def busca_binaria_recursiva(lista, alvo, inicio, fim):
    if inicio > fim:
        return -1

    meio = (inicio + fim) // 2

    if lista[meio] == alvo:
        return meio
    elif alvo < lista[meio]:
        return busca_binaria_recursiva(lista, alvo, inicio, meio - 1)
    else:
        return busca_binaria_recursiva(lista, alvo, meio + 1, fim)



tamanhos = [10, 100, 1000, 10000, 100000]
listas = {}

for tamanho in tamanhos:
    listas[tamanho] = random.sample(range(1, tamanho * 10), tamanho)

print("Listas geradas com sucesso!\n")


alvo = int(input("Digite um número para buscar: "))


for tamanho in tamanhos:
    print(f"\n--- Lista com {tamanho} elementos ---")

    lista = listas[tamanho]

    inicio = time.time()
    resultado_seq = busca_sequencial(lista, alvo)
    fim = time.time()
    tempo_seq = fim - inicio

    lista_ordenada = sorted(lista)

    inicio = time.time()
    resultado_bin = busca_binaria_recursiva(lista_ordenada, alvo, 0, len(lista_ordenada) - 1)
    fim = time.time()
    tempo_bin = fim - inicio


    print("Busca Sequencial:")
    if resultado_seq != -1:
        print(f"Elemento encontrado no índice {resultado_seq}")
    else:
        print("Elemento não encontrado")
    print(f"Tempo: {tempo_seq:.6f} segundos")

    print("\nBusca Binária:")
    if resultado_bin != -1:
        print(f"Elemento encontrado no índice {resultado_bin}")
    else:
        print("Elemento não encontrado")
    print(f"Tempo: {tempo_bin:.6f} segundos")

print("\nFim da execução.")