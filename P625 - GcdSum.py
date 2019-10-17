##  @title      GcdSum
#
#   @brief      Finds sum of the GCD of two values in two ranges modulo 998244353
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=625
#
#   @author     Khalid Abusamieh
#   @date       10/17/2019
#

# Imports
import math

# Value to use in function
val = 10 ** 11

##  @fn     G(N)
#
#   @brief  Formula: G(N) = Sum of gcd(i,j) for [j = 1 -> N] and [i = 1 -> j]
#           Calculated using a nested For loop
#
#   @param  N = number (val)
#
#   @return N/A
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def G(N):
    foo = []
    for j in range(1, N + 1):
        for i in range(1, j + 1):
            foo.append(math.gcd(i,j))

    ans = sum(foo)
    
    return ans

# Answer of function G modulo 998244353
Answer = G(val) % 998244353
print(Answer)
