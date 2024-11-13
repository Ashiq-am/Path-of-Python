# Python code to demonstrate the working of
# next_toward() and normalize()

# importing "decimal" module to use decimal functions
import decimal

# Initializing decimal number
a = decimal.Decimal(101.34)

# Initializing decimal number
b = decimal.Decimal(-101.34)

# Initializing decimal number
c = decimal.Decimal(-58.68)

# Initializing decimal number
d = decimal.Decimal(14.010000000)

# printing the number using next_toward()
print ("The number closest to 1st number in direction of second number : ")
print (a.next_toward(c))

# printing the number using next_toward()
# when equal
print ("The second number with sign of first number is : ",end="")
print (b.next_toward(a))

# printing number after erasing rightmost trailing zeroes
print ("Number after erasing rightmost trailing zeroes : ",end="")
print (d.normalize())
