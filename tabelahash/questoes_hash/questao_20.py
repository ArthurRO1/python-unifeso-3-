class Variavel:
    def __init__(self, nome, tipo, escopo):
        self.nome = nome
        self.tipo = tipo
        self.escopo = escopo

    def __str__(self):
        return f"{self.nome} ({self.tipo}) - {self.escopo}"


class TabelaSimbolos:
    def __init__(self):
        self.tabela = {}

    def declarar(self, nome, tipo, escopo):

        chave = f"{escopo}:{nome}"

        if chave in self.tabela:
            print("Erro: variável já declarada!")
            return

        self.tabela[chave] = Variavel(
            nome,
            tipo,
            escopo
        )

    def buscar(self, nome, escopo):
        chave = f"{escopo}:{nome}"

        return self.tabela.get(chave)

    def listar_escopo(self, escopo):

        for chave, variavel in self.tabela.items():

            if variavel.escopo == escopo:
                print(variavel)


# Teste

ts = TabelaSimbolos()

ts.declarar("idade", "int", "global")
ts.declarar("nome", "string", "global")
ts.declarar("contador", "int", "funcao1")

print(ts.buscar("idade", "global"))

print("\nVariáveis do escopo global:")
ts.listar_escopo("global")