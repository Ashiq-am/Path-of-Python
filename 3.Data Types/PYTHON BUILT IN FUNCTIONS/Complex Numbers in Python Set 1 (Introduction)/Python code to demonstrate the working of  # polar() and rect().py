# Python code to demonstrate the working of
# polar() and rect()

# importing "cmath" for complex number operations
import cmath
import math

# Initializing real numbers
x = 1.0
y = 1.0

# converting x and y into complex number
z = complex(x,y)

# converting complex number into polar using polar()
w = cmath.polar(z)

# printing modulus and argument of polar complex number
print ("The modulus and argument of polar complex number is : ",end="")
print (w)

# converting complex number into rectangular using rect()
w = cmath.rect(1.4142135623730951, 0.7853981633974483)

# printing rectangular form of complex number
print ("The rectangular form of complex number is : ",end="")
print (w)
