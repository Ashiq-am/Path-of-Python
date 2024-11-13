# Python code to demonstrate gcd()
# method exceptions
import math

# prints 0
print("The gcd of 0 and 0 is : ", end="")
print(math.gcd(0, 0))

# Produces error
print("\nThe gcd of a and 13 is : ", end="")
print(math.gcd('a', 13))
