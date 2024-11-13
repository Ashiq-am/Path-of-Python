# Python code to discuss negative
# and non-negative cases

# positive x, positive y (x**y)
print("Positive x and positive y : ",end="")
print(pow(4, 3))

print("Negative x and positive y : ",end="")
# negative x, positive y (-x**y)
print(pow(-4, 3))

print("Positive x and negative y : ",end="")
# positive x, negative y (x**-y)
print(pow(4, -3))

print("Negative x and negative y : ",end="")
# negative x, negative y (-x**-y)
print(pow(-4, -3))
