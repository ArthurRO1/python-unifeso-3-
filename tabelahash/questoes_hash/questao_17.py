class TabelaHashAberta:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [None] * tamanho
        self.n = 0

    def hash(self, chave):
        return chave % self.tamanho

    def inserir(self, chave):
        indice = self.hash(chave)

        while self.tabela[indice] is not None:
            indice = (indice + 1) % self.tamanho

        self.tabela[indice] = chave
        self.n += 1

    def buscar(self, chave):
        indice = self.hash(chave)
        inicio = indice

        while self.tabela[indice] is not None:
            if self.tabela[indice] == chave:
                return indice

            indice = (indice + 1) % self.tamanho

            if indice == inicio:
                break

        return -1

    def remover(self, chave):
        pos = self.buscar(chave)

        if pos != -1:
            self.tabela[pos] = None
            self.n -= 1

    def fator_carga(self):
        return self.n / self.tamanho

    def exibir(self):
        print(self.tabela)
        print("Fator de carga =", self.fator_carga())


# Teste
t = TabelaHashAberta(7)

t.inserir(10)
t.inserir(17)
t.inserir(24)

t.exibir()