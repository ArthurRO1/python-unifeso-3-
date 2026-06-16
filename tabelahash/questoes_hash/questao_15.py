class TabelaHash:
    """
    Tabela Hash com Encadeamento Exterior para tratamento de colisões.
    Utiliza o Método da Divisão como função hash: h(x) = x mod m
    """

    def __init__(self, m: int):
        self.m = m
        # Cada posição é uma lista (encadeamento exterior)
        self.tabela = [[] for _ in range(m)]

    def _hash(self, chave: int) -> int:
        return chave % self.m

    def inserir(self, chave: int) -> None:
        indice = self._hash(chave)
        if chave not in self.tabela[indice]:
            self.tabela[indice].append(chave)

    def buscar(self, chave: int) -> bool:
        indice = self._hash(chave)
        return chave in self.tabela[indice]

    def remover(self, chave: int) -> bool:
        indice = self._hash(chave)
        if chave in self.tabela[indice]:
            self.tabela[indice].remove(chave)
            return True
        return False

    def exibir(self) -> None:
        print(f"\n{'='*40}")
        print(f"Tabela Hash (m={self.m}) - Encadeamento Exterior")
        print(f"{'='*40}")
        for i, lista in enumerate(self.tabela):
            conteudo = " -> ".join(str(c) for c in lista) if lista else "vazio"
            print(f"[{i}]: {conteudo}")
        print(f"{'='*40}\n")


# ─── Demonstração ───────────────────────────────────────────────
if __name__ == "__main__":
    t = TabelaHash(7)

    chaves = [45, 12, 67, 23, 89, 34]
    print("Inserindo chaves:", chaves)
    for c in chaves:
        t.inserir(c)

    t.exibir()

    print("Buscar 23:", t.buscar(23))   # True
    print("Buscar 99:", t.buscar(99))   # False

    print("\nRemovendo 23...")
    t.remover(23)
    t.exibir()
