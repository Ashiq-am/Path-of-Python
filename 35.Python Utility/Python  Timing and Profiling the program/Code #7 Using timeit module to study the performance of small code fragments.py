from timeit import timeit
print (timeit('math.sqrt(2)', 'import math'), "\n")

print (timeit('sqrt(2)', 'from math import sqrt'))
