import unittest 
from main import Calculator

class CalculatorTest(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_plus(self): 
        self.assertEqual(self.calculator.plus(1,1), 2)
    
    
    def test_substruct(self): 
        self.assertEqual(self.calculator.subtraction(3,2), 1)
    
    
    def test_multiply(self): 
        self.assertEqual(self.calculator.multiply(2, 2), 4)
    
    
    def test_divide(self): 
        with self.assertRaises(ZeroDivisionError): 
             self.calculator.divide(3, 0)
        self.assertEqual(self.calculator.divide(6,3), 2)
    
    def test_plus_negative(self):
        self.assertNotEqual(self.calculator.plus(2,3), 7)
    

if __name__ == "__main__":
    unittest.main()