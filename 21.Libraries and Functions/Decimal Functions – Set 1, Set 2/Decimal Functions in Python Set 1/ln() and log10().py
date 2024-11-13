# Python code to demonstrate the working of
# ln() and log10()

# importing "decimal" module to use decimal functions
import decimal

# using ln() to compute the natural log of decimal number
a = decimal.Decimal(4.5).ln()

# using sqrt() to compute the log10 of decimal number
b = decimal.Decimal(4.5).log10()

# printing the natural logarithm
print ("The natural logarithm of decimal number is : ",end="")
print (a)

# printing the log10
print ("The log(base 10) of decimal number is : ",end="")
print (b)
