import os
os.chdir('C:\Users\Owner\DBS\Big Data\CA')

#Test the calculator functionality
import unittest

# Import Calculator program.
from calculator import *

# To test Calculalor program.
class Test_Calculator(unittest.TestCase):

# To test the various calculation funtionalities within the calculation fuction.        
    def test_calculation(self):
    #This test Choice 1: addition functionality.
    # 3 + 4 = 7
    # 4 + 3 = 7
    # 4 + 4 = 8
        self.assertEqual(calculation(4,3,1),('Calculation of 4.00 + 3.00 = 7.00'))
        self.assertEqual(calculation(3,4,1),('Calculation of 3.00 + 4.00 = 7.00'))
        self.assertEqual(calculation(4,4,1),('Calculation of 4.00 + 4.00 = 8.00'))
        
    #This test Choice 2: substraction functionality.
    # 4 - 3 = 1
    # 3 - 4 = -1
    # 3 - 3 = 0        
        self.assertEqual(calculation(4,3,2),('Calculation of 4.00 - 3.00 = 1.00'))
        self.assertEqual(calculation(3,4,2),('Calculation of 3.00 - 4.00 = -1.00'))
        self.assertEqual(calculation(3,3,2),('Calculation of 3.00 - 3.00 = 0.00'))
        
    #This test Choice 3: multiply functionality. 
    # 3 * 4 = 12
    # 4 * 3 = 12
    # 5 * 5 = 25        
        self.assertEqual(calculation(3,4,3),('Calculation of 3.00 * 4.00 = 12.00'))
        self.assertEqual(calculation(4,3,3),('Calculation of 4.00 * 3.00 = 12.00'))
        self.assertEqual(calculation(5,5,3),('Calculation of 5.00 * 5.00 = 25.00'))
        
    #This test Choice 4: divide functionality. 
    # 4 / 3 = 1.33
    # 8 / 4 = 2.00
    # 4 / 4 = 1.00   
        self.assertEqual(calculation(4,3,4),('Calculation of 4.00 / 3.00 = 1.33'))
        self.assertEqual(calculation(8,4,4),('Calculation of 8.00 / 4.00 = 2.00'))
        self.assertEqual(calculation(4,4,4),('Calculation of 4.00 / 4.00 = 1.00'))
        
    #This test Choice 5: exponetiate functionality.
    # 3 ** 4 = 81.00         
    # 4 ** 3 = 64.00 
    # -6 ** 2 = 36.00        
        self.assertEqual(calculation(3,4,5),('Calculation of 3.00 by power of 4.00 = 81.00'))
        self.assertEqual(calculation(4,3,5),('Calculation of 4.00 by power of 3.00 = 64.00'))
        self.assertEqual(calculation(-6,2,5),('Calculation of -6.00 by power of 2.00 = 36.00'))
        
    #This test Choice 6: root functionality.
    # 64 ** (1/6) = 2.00         
    # -27 ** (1/3) = 3.00 
    # 49 ** (1/2)= 7.00        
        self.assertEqual(calculation(6,64,6),('Calculation of 6.00 root of 64.00 = 2.00'))
        self.assertEqual(calculation(3,-27,6),('Calculation of 3.00 root of -27.00 = -3.00'))
        self.assertEqual(calculation(2,49,6),('Calculation of 2.00 root of 49.00 = 7.00'))
        
    #This test Choice 7: combiation (nCr) functionality.
    # 8 C 4 = 70.00         
    # 9 C 3 = 84.00 
    # 6 C 6 = 1.00        
        self.assertEqual(calculation(8,4,7),('Combination of 8 choose 4 = 70.00'))
        self.assertEqual(calculation(9,3,7),('Combination of 9 choose 3 = 84.00'))
        self.assertEqual(calculation(6,6,7),('Combination of 6 choose 6 = 1.00'))
        
    #This test Choice 8: permutation (nPr) functionality.
    # 8 P 4 = 70.00         
    # 9 P 3 = 84.00 
    # 6 P 6 = 720.00        
        self.assertEqual(calculation(8,3,8),('Permutation of 8 choose 3 = 336.00'))
        self.assertEqual(calculation(9,3,8),('Permutation of 9 choose 3 = 504.00'))
        self.assertEqual(calculation(6,6,8),('Permutation of 6 choose 6 = 720.00'))

# To test the various calculation funtionalities within the operation fuction.        
    def test_operation(self):
        
    #This test Choice 9: factorial functionality.
    # 5! = 120        
    # 6! = 720
    # 10! = 3,628,800         
        self.assertEqual(operation(5,9),('Factorial 5! = 120'))
        self.assertEqual(operation(6,9),('Factorial 6! = 720'))
        self.assertEqual(operation(10,9),('Factorial 10! = 3628800'))

    #This test Choice 10:  summation functionality.
    # Summation of 5 = 15     
    # Summation of 10 = 55
    # Summation of 100 = 5050
        self.assertEqual(operation(5,10),('Summation of 5 = 15'))
        self.assertEqual(operation(10,10),('Summation of 10 = 55'))
        self.assertEqual(operation(100,10),('Summation of 100 = 5050'))

    #This test Choice 11: sine functionality.
    # Sine of 90 degrees = 1.000     
    # Sine of -270 degrees = 1.000 
    # Sine of 45 degrees = 0.707       
        self.assertEqual(operation(90,11),('\nSine of 90 degrees = 1.000'))
        self.assertEqual(operation(-270,11),('\nSine of -270 degrees = 1.000'))
        self.assertEqual(operation(45,11),('\nSine of 45 degrees = 0.707'))

    #This test Choice 12: cosine functionality.
    # Cosine of 90 degrees = 0.000     
    # Cosine of -180 degrees = -1.000 
    # Cosine of 45 degrees = 0.707        
        self.assertEqual(operation(90,12),('\nCosine of 90 degrees = 0.000'))
        self.assertEqual(operation(-180,12),('\nCosine of -180 degrees = -1.000'))
        self.assertEqual(operation(45,12),('\nCosine of 45 degrees = 0.707'))

    #This test Choice 13: tan functionality.
    # Tan of 45 degrees = 1.00   
    # Tan of 135 degrees = -1.00
    # Tan of -315 degrees = 1.00 
        self.assertEqual(operation(45,13),('\nTan of 45 degrees = 1.000'))
        self.assertEqual(operation(135,13),('\nTan of 135 degrees = -1.000'))
        self.assertEqual(operation(-315,13),('\nTan of -315 degrees = 1.000'))
        
if __name__ == '__main__':
    unittest.main()