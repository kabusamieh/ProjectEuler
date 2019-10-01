##  @title      DivFactorials
#
#   @brief      Finds the sum of all the multiples of 3 and/or 5 below 1000.
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=549
#
#   @author     Khalid Abusamieh
#   @date       10/01/2019
#
import math

BigNum = 10 ** 8
var = BigNum + 1

##  @fn     s(n)
#
#   @brief  Finds the smallest number m such that n divides m!
#
#   @param  n = Integer to divide by
#
#   @return The smallest number m such that n divides m!
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def s(n):
    for i in range(1,var):
        M = math.factorial(i)
        if M % n == 0:
            break
        
    return i

##  @fn     S(n)
#
#   @brief  Finds the sum of all s(i) in range 2,n
#
#   @param  n = Integer to divide by
#
#   @return The sum of all s(i) in range 2,n
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def S(n):
    foo = []
    for i in range (2,n+1):
        foo.append(s(i))

    bar = sum(foo)

    return bar

#Print the solution
print(S(BigNum))
