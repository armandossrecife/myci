class OperacoesBasicas:
    def adicao(self, valor1, valor2):
        return valor1 + valor2

    def multiplicacao(self, valor1, valor2):
        return valor1*valor2

    def subtracao(self, valor1, valor2):
        return valor1-valor2

    def ler_valores(self):
        print("Operações Básicas:")
        valor1 = float(input("Digite o primeiro número: "))
        valor2 = float(input("Digite o segundo número: "))
        return valor1, valor2
    
    def mostra_menu(self):        
        print("Escolha a operação:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
      
    def executar(self):        
        self.mostra_menu()
        escolha = input("Escolha uma opção: ")
        valor1, valor2 = self.ler_valores()        
        if escolha == '1':
            resultado = self.adicao(valor1, valor2)
        elif escolha == '2':
            resultado = self.subtracao(valor1, valor2)
        elif escolha == '3':
            resultado = self.multiplicacao(valor1, valor2)
        elif escolha == '4':
            print('Não implementado...')
            resultado = 0
        else:
            print("Opção inválida")
            return        
        print("Resultado:", resultado)