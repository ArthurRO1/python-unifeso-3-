class ContadorFrequencias:

    def contar(self, texto):
        frequencias = {}

        palavras = texto.lower().split()

        for palavra in palavras:

            if palavra in frequencias:
                frequencias[palavra] += 1
            else:
                frequencias[palavra] = 1

        return frequencias

    def top_k(self, texto, k):
        freq = self.contar(texto)

        ordenado = sorted(
            freq.items(),
            key=lambda x: x[1],
            reverse=True
        )

        return ordenado[:k]

    def duplicadas(self, lista):
        repetidas = set()

        for item in lista:
            if lista.count(item) > 1:
                repetidas.add(item)

        return list(repetidas)


c = ContadorFrequencias()

texto = "python java python c++ java python"

print(c.contar(texto))
print(c.top_k(texto, 2))

print(c.duplicadas(
    ["Ana", "João", "Ana", "Pedro", "João"]
))