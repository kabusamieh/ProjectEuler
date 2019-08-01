##  @title      LargePrime
#
#   @brief      Finds the largest prime factor of the number 600851475143.
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=3
#
#   @author     Khalid Abusamieh
#   @date       08/01/2019
#
from functools import reduce

####Find largest prime of this!####
val = 600851475143

##  @fn     bigPrime()
#
#   @brief  Finds the largest largest prime factor of a value.
#
#   @return List of prime numbers
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def bigPrime():
    primes = []
    if val > 1:
        for i in range(2,val):
            if (val % i) == 0:
                primes.append(i)
                if reduce(lambda x, y: x*y, primes) == val:
                    break
    return primes

print(max(bigPrime()))
