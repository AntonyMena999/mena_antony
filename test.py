import unittest

class TestSuma(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(2 + 2, 5)  # ❌ Error intencional

class TestTexto(unittest.TestCase):
    def test_texto(self):
        self.assertEqual("Hola", "Chao")  # ❌ Error intencional

if __name__ == '__main__':
    unittest.main()
