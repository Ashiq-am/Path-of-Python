# A Python program that uses Bitwise Not or ~ on boolean
a = True
b = False
print(~a)
print(~b)






"""Reason: The bitwise not operator ~ returns the complement of a number i.e., 
it switches each 1 to 0 and each 0 to 1. Booleans True and False have values 1 and 0 respectively.

˜being the bitwise not operator,

The expression “˜True” returns bitwise inverse of 1.
The expression “˜False” returns bitwise inverse of 0."""









'''Conclusion:
“Logical not or !” is meant for boolean values and “bitwise not or ~” is for integers. Languages like C/C++ and python 
do auto promotion of boolean to integer type when an integer operator is applied. But Java doesn’t do it.'''