import math
import unittest


def wallis(n):
   z= 1
   for i in range(1,n+1):
       a = (4*(i**2))/((4*(i**2))-1)
       z*=a
   return(2*z)
  
from random import *
def monte_carlo(n):
     nod_circle=0
     nod_square=0
     for i in range(n):
         x= random()
         y= random()
         if(x**2 + y**2)<=1:
            nod_circle+= 1
            nod_square+=1
         else:
            nod_square+=1
            
     return(4* nod_circle/nod_square)
     
class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
         def test_accuracy(self):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")

            pi = monte_carlo(i)
           


  
     
 


if __name__ == "__main__":
    unittest.main()
