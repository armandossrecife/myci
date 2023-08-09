import math

class OperacoesLogaritmo:
    def executar(self):
        print("Operações de Logaritmo:")
        base = float(input("Digite o valor da base: "))
        numero = float(input("Digite o valor do número: "))
        resultado = math.log(numero, base)
        print(f"Log base {base} de {numero} é igual a {resultado}")