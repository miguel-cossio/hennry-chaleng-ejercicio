import unittest
import checkpoint as ch
import os
class HenryChallenge(unittest.TestCase):

    def test_ListaDivisibles_01(self):
        lista_test = ch.ListaDivisibles(12, 10)
        lista_esperada = []
        print("Probando caso 1...")
        self.assertEqual(lista_test, lista_esperada)