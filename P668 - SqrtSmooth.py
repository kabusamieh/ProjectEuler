import math

foo = []
bar = []

val = 100

def PrimeMe(n):
    for i in range(1,int(n) + 1):
       if i > 1:
           for j in range(2,i):
               if (i % j) == 0:
                   break
           else:
               foo.append(i)

    return foo

def Smooth():        
    for j in range(1,val + 1):
        o = j
        h = math.sqrt(o)        
        
    for i in PrimeMe(o):
        k = i
        
        if k < h:
            print(k)

Smooth()
