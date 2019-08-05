##  @title      LargeExpo
#
#   @brief      Determine the line number of the highest base/exponent pair.
#               Reference: https://www.python.org/ (open source)
#               Reference: https://projecteuler.net/problem=99
#
#   @author     Khalid Abusamieh
#   @date       08/05/2019
#
import math

file = open("support_files/p099_base_exp.txt","r")
content = file.read()
foo = content.split("\n")

lyst = []
for bar in foo:
    ski = bar.split(",")
    # Using logarithms, the computing time is greatly reduced,
    # as using exponents would produce 3 million digits a piece.
    exp = int(ski[1]) * math.log(int(ski[0]))
    print(exp)
    lyst.append(int(exp))

print("--------------------")
MAX = max(lyst)
print(MAX)

LEN = len(lyst)
print(LEN)

print("--------------------")
# Print MAX's position in lyst +1 to account for list[0]
print(lyst.index(MAX) + 1)
