##  @title      LargePrime
#
#   @brief      Finds the largest prime factor of the number 600851475143.
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=357
#
#   @author     Khalid Abusamieh
#   @date       08/01/2019
#
from functools import reduce

####Find largest prime of this!####
val = 10000

##  @fn     bigPrime()
#
#   @brief  Finds the divisors of a value.
#
#   @return List of divisors
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def getDivs():
    divs = []
    if val > 1:
        for i in range(1,val):
            if (val % i) == 0:
                divs.append(i)

    divs.append(val)
    return divs
            
print(getDivs())

def isPrime(n) : 
    # Corner cases 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
  
    # This is checked so that we can skip  
    # middle five numbers in below loop 
    if (n % 2 == 0 or n % 3 == 0) : 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True

def main():
    prim = []
    chex = []
    for i in getDivs():
        if isPrime(i) == True:
            prim.append(i)

    print(prim)

    for p in prim:
        som = (p+val)/p
        if isPrime(som) == True:
            chex.append(som)

    print(chex)
    print(sum(chex))


main()
