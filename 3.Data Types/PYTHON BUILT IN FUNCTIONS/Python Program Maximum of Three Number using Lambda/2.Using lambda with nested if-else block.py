# Define lambda function
find_max = lambda x, y, z: (x if (x > y and x > z) else y if y > z else z)

num1 = 14
num2 = 15
num3 = 16

# Find maximum using lambda function
result = find_max(num1, num2, num3)

#printing result
print("Maximum number is:", result)
