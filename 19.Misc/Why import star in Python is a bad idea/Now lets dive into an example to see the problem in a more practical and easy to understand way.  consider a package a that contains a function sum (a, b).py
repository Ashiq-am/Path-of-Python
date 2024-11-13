# import the module a using import *
from a import *

# define a function sum
def sum (x, y):
	return x + y

print (sum (2, 6))










'''the error with this code is that the sum function that we define overrides the sum function 
from the module ‘a’ that we imported and we don’t even have any idea about it. also it becomes very 
difficult to identify which function is actually being called in case of large programs.'''
