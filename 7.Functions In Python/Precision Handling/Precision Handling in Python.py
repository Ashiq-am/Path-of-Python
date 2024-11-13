# Python code to demonstrate ceil(), trunc()
# and floor()

# importing "math" for precision function
import math

# initializing value
a = 3.4536

# using trunc() to print integer after truncating
print ("The integral value of number is : ",end="")
print (math.trunc(a))

# using ceil() to print number after ceiling
print ("The smallest integer greater than number is : ",end="")
print (math.ceil(a))

# using floor() to print number after flooring
print ("The greatest integer smaller than number is : ",end="")
print (math.floor(a))







"""Setting Precision"""






# Python code to demonstrate precision
# and round()

# initializing value
a = 3.4536

# using "%" to print value till 2 decimal places
print ("The value of number till 2 decimal place(using %) is : ",end="")
print ('%.2f'%a)

# using format() to print value till 2 decimal places
print ("The value of number till 2 decimal place(using format()) is : ",end="")
print ("{0:.2f}".format(a))

# using round() to print value till 2 decimal places
print ("The value of number till 2 decimal place(using round()) is : ",end="")
print (round(a,2))

