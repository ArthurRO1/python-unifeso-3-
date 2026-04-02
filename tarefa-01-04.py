import random
import time

lista = random.sample(range(1, 100000), 10000)

print("Lista criada")

def busca_sequencial(lista, alvo):
    i = 0
    while i < len(lista):
        if lista[i] == alvo:
            return i
        i += 1
    return -1

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2

        if lista[meio] == alvo:
            return meio
        elif alvo < lista[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return -1

alvo = random.choice(lista)

print(f"Número buscado: {alvo}")

inicio = time.time()
indice_seq = busca_sequencial(lista, alvo)
tempo_seq = time.time() - inicio

lista_ordenada = sorted(lista)

inicio = time.time()
indice_bin = busca_binaria(lista_ordenada, alvo)
tempo_bin = time.time() - inicio

print("\nRESULTADOS:")

print(f"Sequencial -> índice: {indice_seq} | valor: {lista[indice_seq]} | tempo: {tempo_seq:.6f}s")

print(f"Binária    -> índice: {indice_bin} | valor: {lista_ordenada[indice_bin]} | tempo: {tempo_bin:.6f}s")
