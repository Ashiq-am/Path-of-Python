# Python code to swap two numbers
# using Bitwise XOR method


x = 5 # x = 0101
y = 10 # y = 1010

print ("Before swapping: ")
print("Value of x : ", x, " and y : ", y)

# Swap code
x ^= y # x = 1111, y = 1010
y ^= x # y = 0101, x = 1111
x ^= y # x = 1010, y = 0101

print ("After swapping: ")
print("Value of x : ", x, " and y : ", y)
