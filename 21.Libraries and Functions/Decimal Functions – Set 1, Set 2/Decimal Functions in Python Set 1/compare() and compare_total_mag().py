# Python code to demonstrate the working of
# compare() and compare_total_mag()

# importing "decimal" module to use decimal functions
import decimal

# Initializing decimal number
a = decimal.Decimal(9.53)

# Initializing decimal number
b = decimal.Decimal(-9.56)

# comparing decimal numbers using compare()
print ("The result of comparison using compare() is : ",end="")
print (a.compare(b))

# comparing decimal numbers using compare_total_mag()
print ("The result of comparison using compare_total_mag() is : ",end="")
print (a.compare_total_mag(b))
