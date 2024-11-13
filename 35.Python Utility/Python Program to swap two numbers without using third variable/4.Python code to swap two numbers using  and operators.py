# Python code to swap two numbers
# using / and * operators


x = 5.4
y = 10.3

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

# Swap code
x = x * y # x = 55.62, y = 10.3
y = x / y # x = 55.62, y = 5.4
x = x / y # x = 10.3, y = 5.4

print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
