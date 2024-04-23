import unittest

def fibonacci_listas(value):
    values = [0, 1]
    for _ in range(value-1):
        values.append(values[-1] + values[-2])
    return values


class TestFibonacci(unittest.TestCase):
    def test_4(self):
        value = 4
        result = fibonacci(value)
        self.assertEqual(result, 3)
    
    def test_5(self):
        value = 5
        result = fibonacci(value)
        self.assertEqual(result, 5)        
    
    def test_6(self):
        value = 6
        result = fibonacci(value)
        self.assertEqual(result, 8)
    
    def test_7(self):
        value = 7
        result = fibonacci(value)
        self.assertEqual(result, 13)
    
    def test_8(self):
        value = 8
        result = fibonacci(value)
        self.assertEqual(result, 21)
    
    def test_13_with_error(self):
        value = 13
        result = fibonacci(value)
        self.assertEqual(result, 21)

def fibonacci(value):
    anterior = 1
    resultado = 0
    for _ in range(value):
        resultado += anterior
        anterior = resultado - anterior
    return resultado


class TestFibonacci(unittest.TestCase):
    def test_4(self):
        value = 4
        result = fibonacci(value)
        self.assertEqual(result, 3)
    
    def test_5(self):
        value = 5
        result = fibonacci(value)
        self.assertEqual(result, 5)        
    
    def test_6(self):
        value = 6
        result = fibonacci(value)
        self.assertEqual(result, 8)
    
    def test_7(self):
        value = 7
        result = fibonacci(value)
        self.assertEqual(result, 13)
    
    def test_8(self):
        value = 8
        result = fibonacci(value)
        self.assertEqual(result, 21)
    
    def test_13_with_error(self):
        value = 13
        result = fibonacci(value)
        self.assertNotEqual(result, 21)
    
    def test_13_without_error(self):
        value = 13
        result = fibonacci(value)
        self.assertEqual(result, 233)
        
unittest.main()