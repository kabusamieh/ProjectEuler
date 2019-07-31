##  @title      M3n5
#
#   @brief      Finds the sum of all the multiples of 3 and/or 5 below 1000.
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=1
#
#   @author     Khalid Abusamieh
#   @date       07/31/2019
#


##  @fn     multi(m,count)
#
#   @brief  Finds all multiples of an integer and puts them in a list.
#
#   @param  m = Integer whose multiples you seek
#   @param  count = (1000/m) in this case, or just a range.
#
#   @return List of multiples
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def multi(m,count):
    foo = []
    
    for i in range(0,count*m,m):
        if m == 5:
            foo.append(i)
        elif m == 3:
            foo.append(i)
        else:
            print("???")
            break
        
    #print(foo)
    return foo

# Get sum of Multis
var1 = (sum(multi(5,200)))
var2 = (sum(multi(3,334)))

# Print sum of both Multis
print(var1 + var2)
