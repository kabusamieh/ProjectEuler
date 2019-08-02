##  @title      SelfPower
#
#   @brief      Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=48
#
#   @author     Khalid Abusamieh
#   @date       08/02/2019
#

##  @fn     main()
#
#   @brief  Main Function: Finds sum of all self power up to 1000
#
#   @return N/A
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def main():
    foo = []
    for i in range(1,1001):
        j = i
        k = i ** j
        foo.append(k)

    print(sum(foo))
    
main()
