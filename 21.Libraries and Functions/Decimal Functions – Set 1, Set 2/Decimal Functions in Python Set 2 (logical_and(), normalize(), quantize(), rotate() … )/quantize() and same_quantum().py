# Python code to demonstrate the working of
# quantize() and same_quantum()

# importing "decimal" module to use decimal functions
import decimal

# Initializing decimal number
a = decimal.Decimal(20.76548)

# Initializing decimal number
b = decimal.Decimal(12.25)

# Initializing decimal number
c = decimal.Decimal(6.25)

# printing quantized first number
print ("The quantized first number is : ",end="")
print (a.quantize(b))

# checking if both number have same exponent
if (b.same_quantum(c)):
	print ("Both the numbers have same exponent")
else : print ("Both numbers have different exponent")
