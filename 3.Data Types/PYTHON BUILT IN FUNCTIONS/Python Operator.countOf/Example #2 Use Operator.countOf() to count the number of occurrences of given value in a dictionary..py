# Python program showing
# use of countOf() function
# in a dictionary

from operator import *

d = {"score": 3, "score1": 1, "score2": 3, "score3": 1, "score4": 3}

print("Number of occurrence of three in dict =",countOf(d.values(),3))
print("Number of occurrence of one in dict =",countOf(d.values(),1))
print("Number of occurrence of four in dict =",countOf(d.values(),4))
