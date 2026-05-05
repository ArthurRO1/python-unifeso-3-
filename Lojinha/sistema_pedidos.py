# ─────────────────────────────────────────────
#  PRODUTO
# ─────────────────────────────────────────────
class Produto:
    def __init__(self, codigo: int, nome: str, preco: float):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"[{self.codigo}] {self.nome} — R$ {self.preco:.2f}"


# ─────────────────────────────────────────────
#  LISTA LINEAR — Catálogo de Produtos
# ─────────────────────────────────────────────
class Catalogo:
    def __init__(self):
        self._produtos: list = []

    def adicionar_produto(self, produto: Produto):
        self._produtos.append(produto)
        print(f"  Produto adicionado: {produto}")

    def remover_produto(self, codigo: int) -> bool:
        for i, p in enumerate(self._produtos):
            if p.codigo == codigo:
                removido = self._produtos.pop(i)
                print(f"  Produto removido do catálogo: {removido}")
                return True
        print(f"  Produto com código {codigo} não encontrado.")
        return False

    def buscar_por_codigo(self, codigo: int):
        for p in self._produtos:
            if p.codigo == codigo:
                return p
        return None

    def listar(self):
        if not self._produtos:
            print("  Catálogo vazio.")
            return
        print("\n  ── Catálogo de Produtos ──")
        for p in self._produtos:
            print(f"    {p}")

    def esta_vazio(self):
        return len(self._produtos) == 0


# ─────────────────────────────────────────────
#  LISTA LINEAR — Carrinho de Compras
# ─────────────────────────────────────────────
class Carrinho:
    def __init__(self):
        self._itens: list = []

    def adicionar(self, produto: Produto):
        self._itens.append(produto)
        print(f"  Adicionado ao carrinho: {produto}")

    def remover(self, codigo: int) -> bool:
        for i, p in enumerate(self._itens):
            if p.codigo == codigo:
                removido = self._itens.pop(i)
                print(f"  Removido do carrinho: {removido}")
                return True
        print(f"  Produto com código {codigo} não encontrado no carrinho.")
        return False

    def visualizar(self):
        if not self._itens:
            print("  Carrinho vazio.")
            return
        print("\n  ── Itens no Carrinho ──")
        for p in self._itens:
            print(f"    {p}")
        print(f"  Total: R$ {self.total():.2f}")

    def total(self) -> float:
        return sum(p.preco for p in self._itens)

    def esvaziar(self) -> list:
        itens = self._itens.copy()
        self._itens.clear()
        return itens

    def esta_vazio(self) -> bool:
        return len(self._itens) == 0


# ─────────────────────────────────────────────
#  PEDIDO
# ─────────────────────────────────────────────
class Pedido:
    _contador = 1

    def __init__(self, usuario: str, itens: list):
        self.numero = Pedido._contador
        Pedido._contador += 1
        self.usuario = usuario
        self.itens = itens
        self.total = sum(p.preco for p in itens)

    def __str__(self):
        nomes = ", ".join(p.nome for p in self.itens)
        return (f"Pedido #{self.numero} | Cliente: {self.usuario} | "
                f"Itens: [{nomes}] | Total: R$ {self.total:.2f}")


# ─────────────────────────────────────────────
#  FILA — Processamento de Pedidos (FIFO)
# ─────────────────────────────────────────────
class FilaDePedidos:
    def __init__(self):
        self._fila: list = []

    def enfileirar(self, pedido: Pedido):
        self._fila.append(pedido)
        print(f"  Pedido enfileirado: {pedido}")

    def desenfileirar(self):
        if self.esta_vazia():
            print("  Fila de pedidos vazia.")
            return None
        return self._fila.pop(0)

    def visualizar(self):
        if self.esta_vazia():
            print("  Nenhum pedido na fila.")
            return
        print("\n  ── Fila de Pedidos (ordem de chegada) ──")
        for i, pedido in enumerate(self._fila):
            print(f"    {i + 1}º  {pedido}")

    def esta_vazia(self) -> bool:
        return len(self._fila) == 0


# ─────────────────────────────────────────────
#  PILHA — Pagamentos (LIFO)
# ─────────────────────────────────────────────
class PilhaDePagamentos:
    def __init__(self):
        self._pilha: list = []

    def empilhar(self, pedido: Pedido):
        self._pilha.append(pedido)
        print(f"  Pagamento registrado: {pedido}")

    def desempilhar(self):
        if self.esta_vazia():
            print("  Pilha de pagamentos vazia.")
            return None
        pago = self._pilha.pop()
        print(f"  Pagamento processado: {pago}")
        return pago

    def visualizar(self):
        if self.esta_vazia():
            print("  Nenhum pagamento registrado.")
            return
        print("\n  ── Pilha de Pagamentos (topo → base) ──")
        for pedido in reversed(self._pilha):
            print(f"    {pedido}")

    def esta_vazia(self) -> bool:
        return len(self._pilha) == 0


# ─────────────────────────────────────────────
#  HELPERS
# ─────────────────────────────────────────────
def separador(titulo: str):
    print(f"\n{'=' * 50}")
    print(f"  {titulo}")
    print('=' * 50)


def pausar():
    input("\n  Pressione Enter para continuar...")


def ler_int(mensagem: str) -> int:
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("  Entrada inválida. Digite um número inteiro.")


def ler_float(mensagem: str) -> float:
    while True:
        try:
            return float(input(mensagem).replace(",", "."))
        except ValueError:
            print("  Entrada inválida. Digite um valor numérico.")


# ─────────────────────────────────────────────
#  MENUS
# ─────────────────────────────────────────────

def menu_catalogo(catalogo: Catalogo):
    while True:
        separador("GERENCIAR CATÁLOGO")
        print("  1. Adicionar produto")
        print("  2. Remover produto")
        print("  3. Listar produtos")
        print("  0. Voltar")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            print()
            codigo = ler_int("  Código do produto: ")
            if catalogo.buscar_por_codigo(codigo):
                print("  Já existe um produto com esse código.")
            else:
                nome = input("  Nome do produto: ").strip()
                preco = ler_float("  Preço (R$): ")
                catalogo.adicionar_produto(Produto(codigo, nome, preco))
            pausar()

        elif opcao == "2":
            catalogo.listar()
            codigo = ler_int("\n  Código para remover: ")
            catalogo.remover_produto(codigo)
            pausar()

        elif opcao == "3":
            catalogo.listar()
            pausar()

        elif opcao == "0":
            break
        else:
            print("  Opção inválida.")


def menu_carrinho(catalogo: Catalogo, carrinho: Carrinho):
    while True:
        separador("CARRINHO DE COMPRAS")
        print("  1. Adicionar produto ao carrinho")
        print("  2. Remover produto do carrinho")
        print("  3. Visualizar carrinho")
        print("  0. Voltar")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            if catalogo.esta_vazio():
                print("  Catálogo vazio. Cadastre produtos primeiro.")
            else:
                catalogo.listar()
                codigo = ler_int("\n  Código do produto: ")
                produto = catalogo.buscar_por_codigo(codigo)
                if produto:
                    carrinho.adicionar(produto)
                else:
                    print("  Produto não encontrado no catálogo.")
            pausar()

        elif opcao == "2":
            carrinho.visualizar()
            if not carrinho.esta_vazio():
                codigo = ler_int("\n  Código para remover: ")
                carrinho.remover(codigo)
            pausar()

        elif opcao == "3":
            carrinho.visualizar()
            pausar()

        elif opcao == "0":
            break
        else:
            print("  Opção inválida.")


def menu_pedidos(
    carrinho: Carrinho,
    fila: FilaDePedidos,
    pilha: PilhaDePagamentos
):
    while True:
        separador("PEDIDOS E PAGAMENTOS")
        print("  1. Finalizar pedido (carrinho → fila)")
        print("  2. Visualizar fila de pedidos")
        print("  3. Processar próximo pagamento (fila → pilha)")
        print("  4. Visualizar pilha de pagamentos")
        print("  5. Processar TODOS os pagamentos")
        print("  0. Voltar")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            if carrinho.esta_vazio():
                print(
                    "  Carrinho vazio. "
                    "Adicione produtos antes de finalizar."
                )
            else:
                carrinho.visualizar()
                usuario = input("\n  Nome do cliente: ").strip()
                if usuario:
                    itens = carrinho.esvaziar()
                    pedido = Pedido(usuario, itens)
                    fila.enfileirar(pedido)
                    print("  Carrinho esvaziado. Pedido adicionado à fila.")
                else:
                    print("  Nome inválido. Pedido não realizado.")
            pausar()

        elif opcao == "2":
            fila.visualizar()
            pausar()

        elif opcao == "3":
            if fila.esta_vazia():
                print("  Nenhum pedido na fila para processar.")
            else:
                pedido = fila.desenfileirar()
                pilha.empilhar(pedido)
            pausar()

        elif opcao == "4":
            pilha.visualizar()
            pausar()

        elif opcao == "5":
            if fila.esta_vazia():
                print("  Nenhum pedido na fila.")
            else:
                print("\n  Processando todos os pagamentos...")
                while not fila.esta_vazia():
                    pedido = fila.desenfileirar()
                    pilha.empilhar(pedido)
                print("\n  Todos os pedidos foram pagos!")
                pilha.visualizar()
            pausar()

        elif opcao == "0":
            break
        else:
            print("  Opção inválida.")


# ─────────────────────────────────────────────
#  MENU PRINCIPAL
# ─────────────────────────────────────────────
def main():
    catalogo = Catalogo()
    carrinho = Carrinho()
    fila = FilaDePedidos()
    pilha = PilhaDePagamentos()

    # Produtos iniciais para facilitar os testes
    catalogo.adicionar_produto(Produto(101, "Notebook",  3500.00))
    catalogo.adicionar_produto(Produto(102, "Mouse",       89.90))
    catalogo.adicionar_produto(Produto(103, "Teclado",    149.90))
    catalogo.adicionar_produto(Produto(104, "Monitor",   1200.00))
    catalogo.adicionar_produto(Produto(105, "Headset",    299.90))

    while True:
        separador("SISTEMA DE PEDIDOS ONLINE")
        print("  1. Gerenciar Catálogo de Produtos")
        print("  2. Gerenciar Carrinho de Compras")
        print("  3. Pedidos e Pagamentos")
        print("  0. Sair")
        opcao = input("\n  Escolha: ").strip()

        if opcao == "1":
            menu_catalogo(catalogo)
        elif opcao == "2":
            menu_carrinho(catalogo, carrinho)
        elif opcao == "3":
            menu_pedidos(carrinho, fila, pilha)
        elif opcao == "0":
            print("\n  Sistema encerrado. Até logo!\n")
            break
        else:
            print("  Opção inválida.")


if __name__ == "__main__":
    main()
