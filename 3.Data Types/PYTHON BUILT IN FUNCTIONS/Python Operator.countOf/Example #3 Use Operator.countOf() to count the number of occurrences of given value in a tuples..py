# Python program showing
# use of countOf() function
# in a tuples

from operator import *

tup = ( 1, 2, 3, 3, 3 )
tup1 = ( 'a', 'b', 'c', 'b', 'd' )

print("Number of occurrence of b in tuple1 =",countOf(tup1,"b"))
print("Number of occurrence of e in tuple1 =",countOf(tup1,"e"))
print("Number of occurrence of 3 in tuple =",countOf(tup,3))
