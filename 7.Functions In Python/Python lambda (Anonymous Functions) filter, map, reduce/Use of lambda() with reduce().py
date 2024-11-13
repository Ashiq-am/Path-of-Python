# Python code to illustrate
# reduce() with lambda()
# to get sum of a list
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)



"""Here the results of previous two elements are added to the next element and this goes on till the end of the list like 
(((((5+8)+10)+20)+50)+100)."""





'''The reduce() function in Python takes in a function and a list as argument. 
The function is called with a lambda function and a list and a new reduced result is returned. 
This performs a repetitive operation over the pairs of the list. This is a part of functools module'''