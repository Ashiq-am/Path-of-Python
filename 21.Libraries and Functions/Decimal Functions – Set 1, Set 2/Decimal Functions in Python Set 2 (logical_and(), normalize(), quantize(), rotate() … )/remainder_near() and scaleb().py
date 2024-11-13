# Python code to demonstrate the working of
# remainder_near() and scaleb()

# importing "decimal" module to use decimal functions
import decimal

# Initializing decimal number
a = decimal.Decimal(23.765)

# Initializing decimal number
b = decimal.Decimal(12)

# Initializing decimal number
c = decimal.Decimal(8)

# using remainder_near to compute value
print ("The computed value using remainder_near() is : ",end="")
print (b.remainder_near(c))

# using scaleb() to shift exponont
print ("The value after shifting exponent : ",end="")
print (a.scaleb(2))
