# Python code to demonstrate the working of
# next_plus() and next_minus()

# importing "decimal" module to use decimal functions
import decimal

# Initializing decimal number
a = decimal.Decimal(101.34)

# printing the actual decimal number
print ("The original number is : ",end="")
print (a)

# printing number after using next_plus()
print ("The smallest number larger than current number : ",end="")
print (a.next_plus())

# printing number after using next_minus()
print ("The largest number smaller than current number : ",end="")
print (a.next_minus())
