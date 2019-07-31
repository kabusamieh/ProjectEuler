##  @title      EvenFibo
#
#   @brief      Finds the sum of all even Fibonacci numbers up to a cap.
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=2
#
#   @author     Khalid Abusamieh
#   @date       07/31/2019
#
#   [WARNING]   Running with a high val (such as the requested 4 million) will
#               greatly strain a PC.
#

#### Sequence Cap ####
val = 4000000

##  @fn     fibo()
#
#   @brief  Finds all even Fibonacci numbers up to a cap and stores them in a list,
#           it then takes the sum of the list.
#
#   @return N/A
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def fibo():
    foo = []
    i = 0
    j = 1
    count = 0
    
    if val <= 0:
       print("Error, val must be greater than 0")
       
    else:
       print("Sum of Even Fibonacci numbers upto",val,":")
       while count < val:
           k = i + j

           i = j
           j = k
           count += 1

           if i % 2 == 0:
               foo.append(i)
           
    print(sum(foo))

# Function call
fibo()
