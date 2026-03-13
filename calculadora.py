class calculadora:
    def soma(self,x , y):
        return x + y
    
calculadora = calculadora()

x = 5
y = 3

resultado = calculadora.soma(x, y)

print("Soma(orientado objeto): ", resultado)