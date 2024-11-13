# python program to swap two numbers
# using bitwise addition for swapping



x = 5
y = 10

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

# same as x = x + y
x = (x & y) + (x|y)

#vsame as y = x - y
y = x + (~y) + 1

# same as x = x - y
x = x + (~y) + 1

print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)

# This code is contributed by bunnyram19
