##  @title      SumSqrDiv
#
#   @brief      Finds SIGMA2(10^15) modulo 10^9
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=401
#
#   @author     Khalid Abusamieh
#   @date       08/06/2019
#

#### Key values for Problem 401 ####
NUM = 10 ** 15
MOD = 10 ** 9

print(NUM,"&",MOD)

##  @fn     sigma2(n)
#
#   @brief  Finds all divisors of a number 'n' and then takes the sum of all divisors.
#
#   @param  n = Number to find divisors of.
#
#   @return List of divisors
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def sigma2(n):
    foo = []
    bar = []
    for i in range(1,n+1):
        if n % i == 0:
            foo.append(i)

    for j in foo:
        bar.append(j ** 2)

    return bar

##  @fn     SIGMA2(n)
#
#   @brief  SIGMA2 represents the summatory function of sigma2
#
#   @param  n = Number to find the values in.
#
#   @return List of values
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def SIGMA2(n):
    foo = []
    bar = []
    k = 0
    
    for i in range(1,n+1):
        sigi = sum(sigma2(i))
        foo.append(sigi)

    for j in foo:
        k += j
        bar.append(k)

    return bar

# Equation called for by Problem 401
TOT = sum(SIGMA2(NUM)) % MOD
print(TOT)
