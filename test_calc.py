import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        # explicit
        result = calc.add(5,10)
        self.assertEqual(result,15)
        # implicit
        self.assertEqual(calc.add(5,10),15)    
        self.assertEqual(calc.add(-1,-1),-2)
        self.assertEqual(calc.add(1,-1),0)

    def test_subtract(self):
        result = calc.subtract(10,5)
        self.assertEqual(result,5)
        self.assertEqual(calc.subtract(5,10),-5)    
        self.assertEqual(calc.subtract(-1,-1),0)
        self.assertEqual(calc.subtract(1,-1),2)

    def test_multiply(self):
        result = calc.multiply(5,10)
        self.assertEqual(result,50)
        self.assertEqual(calc.multiply(5,10),50)    
        self.assertEqual(calc.multiply(-1,-1),1)
        self.assertEqual(calc.multiply(1,-1),-1)



    def test_divide(self):
        result = calc.divide(5,10)
        # catchesa floor div issue
        self.assertEqual(result,0.5)
        self.assertEqual(calc.divide(5,10),0.5)    
        self.assertEqual(calc.divide(-1,-1),1)
        self.assertEqual(calc.divide(1,-1),-1)
        
        with self.assertRaises(ValueError):
            calc.divide (10,0)

if __name__ == "__main__":
    unittest.main()