import unittest
import checkpoint as ch
import os


class HenryChallenge(unittest.TestCase):

    def test_ListaDivisibles_01(self):
        lista_test = ch.ListaDivisibles(12, 10)
        lista_esperada = []
        print("Probando caso 1...")
        self.assertEqual(lista_test, lista_esperada)

    def test_ListaDivisibles_02(self):
        lista_test = ch.ListaDivisibles(12, 100)
        lista_esperada = [12, 24, 36, 48, 60, 72, 84, 96]
        print("Probando caso 2...")
        self.assertEqual(lista_test, lista_esperada)

    def test_ListaDivisibles_03(self):
        lista_test = ch.ListaDivisibles(3, 9)
        lista_esperada = [3, 6, 9]
        print("Probando caso 3...")
        self.assertEqual(lista_test, lista_esperada)

    def test_Exponente_01(self):
        valor_test = ch.Exponente(10, 2)
        valor_esperado = 100
        print("Probando caso 1 exponentes...")
        self.assertEqual(valor_test, valor_esperado)

    def test_Exponente_02(self):
        valor_test = ch.Exponente(49, 0.5)
        valor_esperado = 7
        print("Probando caso 2 exponentes...")
        self.assertEqual(valor_test, valor_esperado)

    def test_Exponente_03(self):
        valor_test = ch.Exponente(3, 0)
        valor_esperado = 1
        print("Probando caso 3 exponentes...")
        self.assertEqual(valor_test, valor_esperado)

    def test_ListaPrimos_01(self):
        lista_test = ch.ListaPrimos(1, 11)
        lista_esperada = [1, 2, 3, 5, 7, 11]
        self.assertEqual(lista_test, lista_esperada)

    def test_ListaPrimos_02(self):
        lista_test = ch.ListaPrimos('0', 0)
        lista_esperada = None
        self.assertEqual(lista_test, lista_esperada)

    def test_ListaPrimos_03(self):
        lista_test = ch.ListaPrimos(66, 77)
        lista_esperada = [67, 71, 73]
        self.assertEqual(lista_test, lista_esperada)

    def test_ListaPrimos_04(self):
        lista_test = ch.ListaPrimos(0, '66')
        lista_esperada = None
        self.assertEqual(lista_test, lista_esperada)

    def test_ListaDeListas_01(self):
        lista_test = ch.ListaDeListas(100)
        lista_esperada = None
        self.assertEqual(lista_test, lista_esperada)

    def test_ListaDeListas_02(self):
        lista_test = ch.ListaDeListas([1, [2, 3], [[4, 5], 6], [[7]]])
        lista_esperada = [1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(lista_test, lista_esperada)

    def test_ListaDeListas_03(self):
        lista_test = ch.ListaDeListas(
            ['a', 'b', 1, 2, ['a1', 'b3'], [['a'], 2]])
        lista_esperada = ['a', 'b', 1, 2, 'a1', 'b3', 'a', 2]
        self.assertEqual(lista_test, lista_esperada)

    def test_ListaDeListas_04(self):
        lista_test = ch.ListaDeListas([[[1]], 2, [[[[3]]]]])
        lista_esperada = [1, 2, 3]
        self.assertEqual(lista_test, lista_esperada)

    def test_Factorial_01(self):
        valor_test = ch.Factorial(5)
        valor_esperado = 120
        self.assertEqual(valor_test, valor_esperado)

    def test_Factorial_02(self):
        valor_test = ch.Factorial(1)
        valor_esperado = 1
        self.assertEqual(valor_test, valor_esperado)

    def test_Factorial_03(self):
        valor_test = ch.Factorial(0)
        valor_esperado = 1
        self.assertEqual(valor_test, valor_esperado)

    def test_Factorial_04(self):
        valor_test = ch.Factorial(9)
        valor_esperado = 362880
        self.assertEqual(valor_test, valor_esperado)
