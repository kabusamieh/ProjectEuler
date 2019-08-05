##  @title      SumSqrDiff
#
#   @brief      Find the difference between the sum of the squares of the first
#               one hundred natural numbers and the square of the sum.
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=6
#
#   @author     Khalid Abusamieh
#   @date       08/05/2019
#

##  @fn     sumOsquare()
#
#   @brief  Squares numbers in a range and takes the sum of squares.
#
#   @return N/A
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def sumOsquare():
    foo = []
    for i in range(1,101):
        bar = i ** 2
        foo.append(bar)

    return sum(foo)

##  @fn     squareOsum()
#
#   @brief  Takes the sum of a range of numbers and then squares the sum.
#
#   @return N/A
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def squareOsum():
    foo = []
    for i in range(1,101):
        foo.append(i)

    fii = sum(foo)
    bar = fii ** 2

    return bar

# Find the difference
bigDiff = sumOsquare() - squareOsum()
print(abs(bigDiff))
