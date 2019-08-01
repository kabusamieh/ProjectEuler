##  @title      M3n5
#
#   @brief      Finds the sum of all the multiples of 3 and/or 5 below 1000.
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=1
#
#   @author     Khalid Abusamieh
#   @date       07/31/2019
#


##  @fn     multi(m)
#
#   @brief  Finds all multiples of an integer and puts them in a list.
#
#   @param  m = Integer whose multiples you seek
#
#   @return List of multiples
#
#   @author Khalid Abusamieh
#
#   @note   N/A
#
def multi(m):
    foo = []
    
    for i in range(0,1000,m):
        if m == 5:
            foo.append(i)
        elif m == 3:
            foo.append(i)
        else:
            print("???")
            break
        
    #print(foo)
    return foo

fiv = multi(5)
thr = multi(3)

infiv = set(fiv)
inthr = set(thr)

fivthrunq = inthr - infiv

result = fiv + list(fivthrunq)
print(sum(result))
