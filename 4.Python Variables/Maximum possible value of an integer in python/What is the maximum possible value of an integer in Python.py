'''Consider below Python program.'''


# A Python program to demonstrate that we can store
# large numbers in Python

x = 10000000000000000000000000000000000000000000
x = x + 1
print (x)




"""In Python, value of an integer is not restricted by the number of bits and can expand to the
limit of the available memory (Sources : this and this). 

Thus we never need any special arrangement for storing large numbers (Imagine doing above arithmetic in C/C++)."""





"""As a side note, in Python 3, there is only one type “int” for all type of integers. 
In Python 2.7. there are two separate types “int” (which is 32 bit) and “long int” that is same as “int” of Python 3.x, i.e., 
can store arbitrarily large numbers."""





# A Python program to show that there are two types in
# Python 2.7 : int and long int
# And in Python 3 there is only one type : int

x = 10
print(type(x))

x = 10000000000000000000000000000000000000000000
print(type(x))







"""We may want to try more interesting programs like below"""

# Printing 100 raise to power 100
print(100**100)
