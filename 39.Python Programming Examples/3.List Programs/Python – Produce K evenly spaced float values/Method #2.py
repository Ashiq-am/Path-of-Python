# Python3 code to demonstrate working of
# Produce K evenly spaced float values
# Using loop

# initializing range
i, j = 2, 10

# Initialize K
K = 15

# computing difference
diff = (j - i) / K

# using list comprehension to formulate elements
res = [i + (diff * idx) for idx in range(1, K + 1)]

# printing result
print("The constructed list : " + str(res))
