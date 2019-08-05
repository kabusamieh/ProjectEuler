##  @title      SmallMulti
#
#   @brief      Finds the smallest evenly divisible number by a range.
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=5
#
#   @author     Khalid Abusamieh
#   @date       08/05/2019
#

##  @fn     checkDiv(n, lst)
#
#   @brief  Checks for a lack of remainder.
#
#   @param  n = Number
#   @param  lst = List of numbers to divide by.
#
#   @return N/A
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def checkDiv(n, lst):
    return all(map(lambda y: n%y == 0, lst))

##  @fn     main()
#
#   @brief  Main Function
#
#   @return N/A
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def main():
    foo = []
    for h in range(1,21):
        foo.append(h)

    i = 0
    while True:
        i += 10

        if checkDiv(i, foo) == True:
            print(i)
            break

# Function call
main()
