import aritmetica
import trigonometria
import logaritmo

class CalculadoraCientifica:
    opcao = 0
    def __init__(self):
        self.opcoes = {
            1: aritmetica.OperacoesBasicas(),
            2: trigonometria.OperacoesTrigonometricas(),
            3: logaritmo.OperacoesLogaritmo()
        }
    
    def mostrar_menu(self):
        print("Calculadora Científica")
        print("Menu de Opções:")
        print("1 - Operações Básicas")
        print("2 - Operações Trigonométricas")
        print("3 - Operações de Logaritmo")
    
    def executar(self):
        while True:
            self.mostrar_menu()
            self.opcao = int(input("Escolha uma opção: "))
            if self.opcao in self.opcoes:
                self.opcoes[self.opcao].executar()
            else:
                print("Opção inválida")
            
            continuar = input("Deseja continuar? (S/N): ")
            if continuar.lower() != 's':
                break

calculadora = CalculadoraCientifica()
calculadora.executar()