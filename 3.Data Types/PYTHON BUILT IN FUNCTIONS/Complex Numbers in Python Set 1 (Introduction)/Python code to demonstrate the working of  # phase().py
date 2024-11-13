# Python code to demonstrate the working of
# phase()

# importing "cmath" for complex number operations
import cmath

# Initializing real numbers
x = -1.0
y = 0.0

# converting x and y into complex number
z = complex(x,y)

# printing phase of a complex number using phase()
print ("The phase of complex number is : ",end="")
print (cmath.phase(z))
