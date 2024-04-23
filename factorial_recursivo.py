import unittest


def factorial_recursivo(value):
    if value <= 1:
        return (1)
    else:
        return (value * factorial_recursivo(value-1))


class TestFactorial(unittest.TestCase):
    
    def test_1_correct(self):
        value = 1
        result = factorial_recursivo(value)
        self.assertEqual(result, 1)
    
    def test_2_correct(self):
        value = 2
        result = factorial_recursivo(value)
        self.assertEqual(result, 2)
    
    def test_6_correct(self):
        value = 6
        result = factorial_recursivo(value)
        self.assertEqual(result, 720)
    
    def test_3(self):
        value = 3
        result = factorial_recursivo(value)
        self.assertEqual(result, 6)
    
    def test_4(self):
        value = 4
        result = factorial_recursivo(value)
        self.assertEqual(result, 24)        
    
    def test_5(self):
        value = 5
        result = factorial_recursivo(value)
        self.assertEqual(result, 120)
    
    def test_7_with_error(self):
        value = 7
        result = factorial_recursivo(value)
        self.assertNotEqual(result, 5039)
    
    def test_7_correct(self):
        value = 7
        result = factorial_recursivo(value)
        self.assertEqual(result, 5040)
    

        
unittest.main()