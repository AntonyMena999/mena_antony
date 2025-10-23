import unittest

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(2 + 2, 4)  #Corregido

class TestTexto(unittest.TestCase):
    def test_texto(self):
        self.assertEqual("Hola", "Hola")  #Corregido

if __name__ == '__main__':
    unittest.main()
