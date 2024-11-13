# Python3 code to demonstrate
# to multiply numbers with position
# and add them to return num


# initialising list
ini_list = [[3, 4, 7], [6, 7, 8], [10, 7, 5], [11, 12, 13]]

# printing initial_list
print("initial_list ", ini_list)

# Using list comprehension
res = [sum(i * j for i, j in enumerate(sublist))
       for sublist in ini_list]

# printing result
print("result", res)

