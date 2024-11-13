# Python code to demonstrate the working of
# copy_abs(),copy_sign() and copy_negate()

# importing "decimal" module to use decimal functions
import decimal

# Initializing decimal number
a = decimal.Decimal(9.53)

# Initializing decimal number
b = decimal.Decimal(-9.56)

# printing absolute value using copy_abs()
print ("The absolute value using copy_abs() is : ",end="")
print (b.copy_abs())

# printing negated value using copy_negate()
print ("The negated value using copy_negate() is : ",end="")
print (b.copy_negate())

# printing sign effected value using copy_sign()
print ("The sign effected value using copy_sign() is : ",end="")
print (a.copy_sign(b))
