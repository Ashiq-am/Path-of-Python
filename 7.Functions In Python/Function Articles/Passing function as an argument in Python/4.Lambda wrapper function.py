# Defining lambda function
square = lambda x:x * x

# Defining lambda function
# and passing function as an argument
cube = lambda func:func**3


print("square of 2 is :"+str(square(2)))
print("\nThe cube of "+str(square(2))+" is " +str(cube(square(2))))
