from par import eh_par

import unittest

class TestPar(unittest.TestCase):
    def test_par(self):
        self.assertTrue(eh_par(4))
    
    def test_impar(self):
        self.assertFalse(eh_par(3))


if __name__ == '__main__':
    unittest.main()