# Questão 16 - Método da Multiplicação com Encadeamento Exterior

tamanho = 10
tabela = [[] for _ in range(tamanho)]

def hash_multiplicacao(chave):
    A = 0.6180339887
    return int(tamanho * ((chave * A) % 1))

def inserir(chave):
    indice = hash_multiplicacao(chave)
    tabela[indice].append(chave)

def buscar(chave):
    indice = hash_multiplicacao(chave)

    if chave in tabela[indice]:
        print("Chave encontrada no índice", indice)
    else:
        print("Chave não encontrada")

def remover(chave):
    indice = hash_multiplicacao(chave)

    if chave in tabela[indice]:
        tabela[indice].remove(chave)
        print("Chave removida")

def exibir():
    print("\nTabela Hash")

    for i in range(tamanho):
        print(i, ":", tabela[i])


# Teste

inserir(10)
inserir(20)
inserir(30)
inserir(40)

exibir()

buscar(20)

remover(20)

exibir()