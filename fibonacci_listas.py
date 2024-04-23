import unittest

def fibonacci_listas(value):
    values = [0, 1]
    for _ in range(value-1):
        values.append(values[-1] + values[-2])
    return values[-1]

class TestFibonacci_listas(unittest.TestCase):
    def test_4(self):
        value = 4
        result = fibonacci_listas(value)
        self.assertEqual(result, 3)
    
    def test_5_with_Error(self):
        value = 5
        result = fibonacci_listas(value)
        self.assertNotEqual(result, 100)       
    
    def test_5_correct(self):
        value = 5
        result = fibonacci_listas(value)
        self.assertEqual(result, 5)  
    
    def test_6(self):
        value = 6
        result = fibonacci_listas(value)
        self.assertEqual(result, 8)
    
    def test_7(self):
        value = 7
        result = fibonacci_listas(value)
        self.assertEqual(result, 13)
    
    def test_8(self):
        value = 8
        result = fibonacci_listas(value)
        self.assertEqual(result, 21)
    
    def test_13_with_error(self):
        value = 13
        result = fibonacci_listas(value)
        self.assertNotEqual(result, 21)
    
    def test_10(self):
        value = 10
        result = fibonacci_listas(value)
        self.assertEqual(result, 55)

unittest.main()