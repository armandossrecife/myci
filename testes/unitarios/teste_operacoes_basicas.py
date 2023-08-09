import unittest
import operacoes.aritmetica as aritmetica

class TestOperacoesBasicas(unittest.TestCase):
    def setUp(self):
        self.operacoes = aritmetica.OperacoesBasicas()
    
    def test_adicao(self):
        resultado = self.operacoes.adicao(5, 3)
        self.assertEqual(resultado, 8)
