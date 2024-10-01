
class Aritmetica:
    
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
    
    def suma(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB
    
    def multiplicacion(self):
        return self.operandoA * self.operandoB
    
    def dividir(self):
        return self.operandoA / self.operandoB

aritmetica1 = Aritmetica(5, 6)

print(aritmetica1.suma())
print(aritmetica1.resta())
print(aritmetica1.multiplicacion())
print(f'{aritmetica1.dividir():.2f}') # si se imprime con fstring y se suma " :.2f " solo imprime dos numeros despues de la coma en caso de numeros flotantes
