import time

class Cache:
    def __init__(self):
        self.cache = {}

    def funcao_custosa(self, numero):

        if numero in self.cache:
            print("Resultado veio do CACHE")
            return self.cache[numero]

        print("Calculando...")
        time.sleep(2)

        resultado = numero ** 2

        self.cache[numero] = resultado

        return resultado


cache = Cache()

print(cache.funcao_custosa(10))
print(cache.funcao_custosa(10))
print(cache.funcao_custosa(20))