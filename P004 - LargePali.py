##  @title      LargePali
#
#   @brief      Finds the largest palindrome made from the product of two 3-digit numbers.
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=4
#
#   @author     Khalid Abusamieh
#   @date       08/01/2019
#

##  @fn     bigPalindrome()
#
#   @brief  Finds the largest palindrome made from the product of two 3-digit numbers.
#
#   @return List of palindromes
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def bigPalindrome():
    palis = []
    for i in range(1000):
        if len(str(i)) == 3:
            for n in range(1000):
                if len(str(n)) == 3:
                    j = i * n
                    k = str(j)
                    if k == k[::-1]:
                        palis.append(j)

    return palis

print(max(bigPalindrome()))
