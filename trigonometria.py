import math

class OperacoesTrigonometricas:
    def seno(self, angulo):
        return math.sin(math.radians(angulo))

    def ler_angulo(self):
        angulo = float(input("Digite o ângulo em graus: "))
        return angulo

    def mostra_menu(self):
        print("Escolha a operação:")
        print("1 - Seno")
        print("2 - Cosseno")
        print("3 - Tangente")
      
    def executar(self):
        self.mostra_menu()
        escolha = input("Escolha uma opção: ")
        angulo = self.ler_angulo()
        if escolha == '1':
            resultado = self.seno(angulo)
        elif escolha == '2':
            print('Não implementado...')
            resultado = 0
        elif escolha == '3':
            print('Não implementado...')
            resultado = 0
        else:
            print("Opção inválida")
            return        
        print("Resultado:", resultado)