##  @title      SpecPythTriple
#
#   @brief      Finds the product of abc where a + b + c = 1000
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=9
#
#   @author     Khalid Abusamieh
#   @date       08/05/2019
#
import math

##  @fn     pythTriplet(n)
#
#   @brief  Find the product of abc where a + b + c = 1000
#
#   @param  n = Number to act as range.
#
#   @return N/A
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def pythTriplet(n):
    for b in range(n):
        for a in range (1,b):
            c = math.sqrt( a * a + b * b)
            pythaT = a + b + int(c)
            if c % 1 == 0:
                if pythaT == 1000:
                    print(a, b, int(c), pythaT)
                    foo = (a * b * int(c))
                    print(foo)
                    break
                
# Call function with large enough number for parameter
pythTriplet(500)
